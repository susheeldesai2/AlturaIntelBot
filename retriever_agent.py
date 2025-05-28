from graph.state import AgentState
from utils.embedding import embed_text
from utils.pinecone_index import index

def retriever_agent(input: AgentState) -> AgentState:
    question = input["question"]
    targets = input["routing_info"].get("targets", [])

    embedding = embed_text([question])[0]
    all_chunks = []

    for target in targets:
        results = index.query(
            vector=embedding.tolist(),
            top_k=10,
            include_metadata=True,
            filter={"source": target}
        )

        chunks = [
            match.metadata["text"]
            for match in results.matches
            if match.metadata.get("source") == target
        ]

        print(f"\n🔍 Retrieved {len(chunks)} chunks from: {target}")
        all_chunks.extend(chunks)

    return {
        "retrieved_chunks": all_chunks,
        "trace_log": input.get("trace_log", []) + [
            f"Retriever fetched {len(all_chunks)} chunks from: {', '.join(targets)}"
        ]
    }
