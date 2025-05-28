from graph.state import AgentState
from langchain_groq import ChatGroq

llm = ChatGroq(temperature=0, model="llama3-70b-8192")

def router_agent(input: AgentState) -> AgentState:
    question = input["question"]

    prompt = (
        "You are an internal assistant at AlturaTech. Route the user's question to one of the following documents:\n\n"
        "- HR_Handbook.pdf\n"
        "- Security_Protocol.pdf\n"
        "- Sales_Playbook.pdf\n"
        "- Engineering_SOPs (HTML)\n\n"
        "Respond ONLY with the file name that is most relevant to the question.\n\n"
        f"Question: {question}"
    )

    response = llm.invoke(prompt)
    predicted_doc = response.content.strip()

    # Validate known doc names, else mark UNKNOWN
    known_docs = {
        "HR_Handbook.pdf",
        "Security_Protocol.pdf",
        "Sales_Playbook.pdf",
        "Engineering_SOPs"
    }

    if predicted_doc not in known_docs:
        predicted_doc = "UNKNOWN"

    return {
        "routing_info": {"target": predicted_doc},
        "trace_log": [f"Router (LLM) routed to {predicted_doc}"]
    }
