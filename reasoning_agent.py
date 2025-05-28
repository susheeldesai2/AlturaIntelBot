from langchain_groq import ChatGroq
from graph.state import AgentState

llm = ChatGroq(temperature=0, model="llama3-70b-8192")

def reasoning_agent(input: AgentState) -> AgentState:
    question = input["question"]
    chunks = input.get("retrieved_chunks", [])

    context = "\n---\n".join(chunks)

    prompt = (
        "You are an internal policy assistant at AlturaTech.\n\n"
        "Use the provided context to answer the question clearly and accurately. The context may come from multiple internal documents "
        "such as HR handbooks, security protocols, or engineering SOPs.\n\n"
        "Your responsibilities:\n"
        "- Reference the content closely — do not invent policies that aren't grounded in the context.\n"
        "- If multiple interpretations exist, prioritize the stricter policy.\n"
        "- If the exact answer isn’t present, infer only from similar statements.\n"
        "- Be concise, professional, and follow an internal-facing tone.\n"
        "- Avoid speculation or placeholders like 'maybe' or 'possibly'.\n"
        "- If context seems irrelevant or insufficient, state clearly: 'Insufficient context to answer precisely.'\n\n"
        f"Question: {question}\n\nContext:\n{context}"
    )

    response = llm.invoke(prompt)

    return {
        "reasoning": response.content,
        "trace_log": input.get("trace_log", []) + ["Reasoning completed via Groq"]
    }
