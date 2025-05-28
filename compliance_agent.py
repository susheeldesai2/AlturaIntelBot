from graph.state import AgentState

def compliance_agent(input: AgentState) -> AgentState:
    answer = input["reasoning"]

    # Simple static check
    if "confidential" in answer.lower():
        answer += "\n\n⚠️ This answer may contain sensitive content."

    return {
        "compliance_checked": answer,
        "trace_log": input.get("trace_log", []) + ["Compliance check complete"]
    }
