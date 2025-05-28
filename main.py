from graph.graph import graph

def run_pipeline(question: str):
    input_state = {
        "question": question,
        "routing_info": {},
        "retrieved_chunks": [],
        "reasoning": "",
        "compliance_checked": "",
        "trace_log": []
    }

    result = graph.invoke(input_state)

    # Final output: either from Reasoning or Compliance (if redacted/modified)
    final_output = result.get("compliance_checked") or result.get("reasoning") or "⚠️ No answer generated."

    print("\nFinal Answer:\n")
    print(final_output)

    print("\nAgent Trace Log:")
    for step in result.get("trace_log", []):
        print("  -", step)


if __name__ == "__main__":
    while True:
        question = input("\n💬 Ask a company policy question (or type 'exit'): ")
        if question.lower() in ["exit", "quit", "q"]:
            print("Session ended.")
            break
        run_pipeline(question)
