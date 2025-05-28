from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-small-en")

def embed_text(texts):
    return model.encode(texts, normalize_embeddings=True)