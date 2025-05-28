import os
from utils.loader import load_pdf, load_html
from utils.chunker import chunk_text
from utils.embedding import embed_text
from utils.pinecone_index import upsert_chunks

PDF_DIR = "docs"
HTML_URL = "https://datasense78.github.io/engineeringsop/"

for filename in os.listdir(PDF_DIR):
    if filename.endswith(".pdf"):
        print(f"\n📄 Processing file: {filename}")
        file_path = os.path.join(PDF_DIR, filename)
        text = load_pdf(file_path)
        print(f"🔍 Extracted text length: {len(text)} characters")
        chunks = chunk_text(text)
        embeddings = embed_text(chunks)
        upsert_chunks(chunks, embeddings, metadata_base={"source": filename})

print("\n🌐 Scraping Engineering SOPs HTML...")
html_text = load_html(HTML_URL)
print(f"🔍 Extracted HTML length: {len(html_text)} characters")
html_chunks = chunk_text(html_text)
html_embeddings = embed_text(html_chunks)
upsert_chunks(html_chunks, html_embeddings, metadata_base={"source": "Engineering_SOPs"})

print("\n✅ All documents embedded and stored in Pinecone.")