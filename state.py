from typing import TypedDict

class AgentState(TypedDict):
    question: str
    routing_info: dict
    retrieved_chunks: list
    reasoning: str
    compliance_checked: str
    trace_log: list