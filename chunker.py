from langchain.text_splitter import CharacterTextSplitter

def chunk_text(text, chunk_size=500, overlap=50):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=chunk_size,
        chunk_overlap=overlap,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    # for i in range(len(chunks)):
    #     print(f"Chunk {i+1}: {chunks[i]}")
    return chunks
