from graph.state import AgentState
from langchain_groq import ChatGroq

llm = ChatGroq(temperature=0, model="llama3-70b-8192")

DOCUMENTS = {
    "HR_Handbook.pdf": (
        "Covers employee lifecycle policies including probation, leave structure, bonuses, "
        "internal transfers, exit protocols, upskilling, and confidentiality rules."
    ),
    "Security_Protocol.pdf": (
        "Outlines internal security architecture, zero trust protocols, device tagging, role-based access control, "
        "incident escalation procedures, and digital forensics triggers."
    ),
    "Sales_Playbook.pdf": (
        "Provides enterprise sales strategies, client segmentation, discount rules, high-risk client filters, "
        "rejection scripts, and internal-only reporting KPIs."
    ),
    "Engineering_SOPs": (
        "Details standard operating procedures for engineering workflows, code deployments, production access, "
        "tool usage, and dev best practices. (HTML)"
    )
}

def router_agent(input: AgentState) -> AgentState:
    question = input["question"]

    doc_descriptions = "\n".join(
        f"- {name}: {desc}" for name, desc in DOCUMENTS.items()
    )

    prompt = (
        "You are an internal assistant at AlturaTech. Based on the user's question, identify all relevant documents "
        "from the list below that might help answer it.\n\n"
        f"{doc_descriptions}\n\n"
        "Respond ONLY with a Python list of document names. If none are relevant, return an empty list.\n\n"
        f"Question: {question}"
    )

    response = llm.invoke(prompt)

    try:
        predicted_docs = eval(response.content.strip())
    except Exception:
        predicted_docs = []

    known_docs = set(DOCUMENTS.keys())
    predicted_docs = [doc for doc in predicted_docs if doc in known_docs]

    return {
        "routing_info": {"targets": predicted_docs},
        "trace_log": [f"Router (LLM) routed to: {', '.join(predicted_docs) or 'None'}"]
    }
