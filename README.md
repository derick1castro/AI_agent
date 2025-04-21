# 🧠 LLM Retrieval QA Prototype

**Ask natural language questions. Get fast, precise, and contextual answers using FAISS and GPT-4.**

---

## ✨ Overview

This is a simple and functional prototype for _LLM QA Retrieval_ that:

✅ Accepts natural language questions  
✅ Searches for the most relevant answer using FAISS (vector search)  
✅ Uses GPT-4 to generate an answer based on the retrieved context

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/derick1castro/AI_agent.git
cd AI_agent
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

> ⚠️ **Make sure you're using Python 3.11.9**

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your OpenAI API Key

Create a `.env` file in the project root with the following content:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 5. Prepare your dataset

Create a `data/dataset.json` file in the following format:

```json
[
  { "id": 1, "text": "The property tax rate in Travis County is 1.9% as of 2023." },
  { "id": 2, "text": "GPT-4 is the most advanced language model by OpenAI." }
]
```

### 6. Run the application

```bash
python main.py
```

### 7. Ask questions like:

```
Who is the COVID-19 vaccine recommended for?
```

---

## How It Works

- Uses OpenAI's `text-embedding-3-small` model to convert texts into vectors  
- Indexes vectors using **FAISS** for fast similarity search  
- Retrieves the most relevant context snippets  
- Uses GPT-4 to generate an answer **only** from that context  
- Logs operations using **loguru** in `logs/app.log`

---

## What I'd Do Next With More Time

- Add support for PDF and text file ingestion (using LangChain or PyMuPDF).
- Implement a web interface (e.g., Flask or Streamlit).
- Switch to a local embedding model for offline use.
- Improve retrieval with metadata filtering or hybrid search (keyword + vector).
- Add a caching layer for repeated queries and faster responses. 

---

---
