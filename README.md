# 🛡️ AlturaIntelBot

**AlturaPolicyAgent** is a multi-agent, LLM-powered internal assistant designed to help AlturaTech employees query internal documents like HR handbooks, security protocols, SOPs, and sales playbooks. It uses intelligent document routing, vector search, and reasoning to deliver grounded, policy-aligned answers.

---

## Features

- **LLM-Powered Router** — routes questions to relevant documents automatically
- **Retriever + Pinecone Index** — fetches top-matching document chunks
- **Reasoning Agent** — answers questions using context with precision
- ⚖**Compliance Checker** — flags sensitive content (e.g. "confidential")
- **Multi-source Retrieval** — combines context across HR, Security, Sales & SOPs

---

## Project Structure

```bash
altura-policy-agent/
├── agents/
│   ├── router_agent.py       # Document routing using LLM + descriptions
│   ├── retriever_agent.py    # Vector search from Pinecone
│   ├── reasoning_agent.py    # Final answer generation
│   └── compliance_agent.py   # Sensitive content check
│
├── docs/                     # Source documents (PDFs)
│   ├── HR_Handbook.pdf
│   ├── Security_Protocol.pdf
│   └── Sales_Playbook.pdf
│
├── graph/
│   ├── graph.py              # LangGraph flow logic
│   └── state.py              # Shared AgentState type
│
├── scripts/
│   └── embed_docs.py         # Chunking + embedding + Pinecone upsert
│
├── utils/
│   ├── chunker.py            # Chunking logic
│   ├── embedding.py          # BAAI embedding model
│   ├── loader.py             # PDF/HTML document loader
│   └── pinecone_index.py     # Pinecone index interface
│
├── main.py                   # CLI entry point for the assistant
└── README.md
```

---

## 🧠 How It Works

1. **Documents** are loaded and chunked.
2. Each chunk is embedded using the `BAAI/bge-small-en` model.
3. Embeddings are upserted into Pinecone with metadata (e.g. `"source": "HR_Handbook.pdf"`).
4. User question flows through:
   - Router → Retriever → Reasoner → Compliance → Output
5. Context-aware answer is returned with optional compliance warnings.

---

## ⚙️ Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/your-org/AlturaPolicyAgent.git
cd AlturaPolicyAgent
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment
Set your Pinecone and Groq API keys:
```bash
export PINECONE_API_KEY=...
export PINECONE_ENVIRONMENT=...
export GROQ_API_KEY=...
```

### 4. Embed All Documents
```bash
python scripts/embed_docs.py
```

This loads, chunks, embeds, and uploads all document data to Pinecone.

### 5. Run the Assistant
```bash
python main.py
```
Then ask a question like:
```text
💬 Ask a company policy question: What’s the leave policy for employees over 3 years?
```

---

## Sample Questions

- "What is the exit process for confirmed employees?"
- "What are the conditions for remote work and device compliance?" *(multi-doc)*
- "How are critical security incidents escalated?"
- "Can engineers switch to other verticals internally?"

---

## Notes
- This system is for **internal use only**.
- Answers are grounded in internal AlturaTech documents.
- Compliance checks are advisory; enforcement logic can be expanded.

---

## 📌 Roadmap Ideas
- [ ] Add citation trace (e.g. "based on HR_Handbook")
- [ ] GUI or web-based frontend
- [ ] Role-based document access control
- [ ] Vector namespace separation

---

## 🧾 License
Internal use only © AlturaTech Solutions Pvt. Ltd.
