from langgraph.graph import StateGraph, END
from graph.state import AgentState
from agents.router_agent import router_agent
from agents.retriever_agent import retriever_agent
from agents.reasoning_agent import reasoning_agent
from agents.compliance_agent import compliance_agent

# Build the graph
graph_builder = StateGraph(AgentState)

graph_builder.add_node("Router", router_agent)
graph_builder.add_node("Retriever", retriever_agent)
graph_builder.add_node("Reasoner", reasoning_agent)
graph_builder.add_node("Compliance", compliance_agent)
graph_builder.add_node("END", lambda x: x)  # ✅ Define the END node

graph_builder.set_entry_point("Router")

# Updated conditional logic for multi-target routing
def route_or_end(input: AgentState) -> str:
    targets = input["routing_info"].get("targets", [])
    if not targets:
        return "END"
    return "Retriever"

graph_builder.add_conditional_edges(
    "Router",
    route_or_end,
    {
        "Retriever": "Retriever",
        "END": "END"
    }
)

graph_builder.add_edge("Retriever", "Reasoner")
graph_builder.add_edge("Reasoner", "Compliance")

graph = graph_builder.compile()

if __name__ == "__main__":
    graph.get_graph().draw_mermaid_png(output_file_path="graph.png")
    print("✅ Mermaid graph generated at graph.png")
