# RAG System Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         RAG System Architecture                          │
└─────────────────────────────────────────────────────────────────────────┘

                              ┌──────────────┐
                              │    User      │
                              │   Question   │
                              └──────┬───────┘
                                     │
                                     ▼
                    ┌────────────────────────────────┐
                    │    1. EMBEDDING SERVICE        │
                    │  (Convert question to vector)  │
                    │                                │
                    │  Model: qwen3-embedding        │  ◄─── Change here!
                    │  URL: http://127.0.0.1:8888   │       (embedding notebook)
                    └────────────┬───────────────────┘
                                 │
                                 ▼
                    ┌────────────────────────────────┐
                    │    2. MILVUS VECTOR DB         │
                    │   (Search similar documents)   │
                    │                                │
                    │  Retrieves: Top 5 documents    │
                    │  Threshold: > 0.7 similarity   │
                    └────────────┬───────────────────┘
                                 │
                                 ▼
                    ┌────────────────────────────────┐
                    │    3. RERANKER MODEL           │
                    │   (Score document relevance)   │
                    │                                │
                    │  Model: qwen3-reranker         │  ◄─── Change here!
                    │  Path: Line 118 in notebook    │       (cell [6])
                    │  Keeps: Score > 0.9            │
                    └────────────┬───────────────────┘
                                 │
                                 ▼
                    ┌────────────────────────────────┐
                    │    4. AGENT MODEL              │
                    │   (Generate final answer)      │
                    │                                │
                    │  Model: qwen3-0.6b            │  ◄─── CHANGE HERE!
                    │  Path: Line 273 in notebook    │       (cell [15])
                    │  Max tokens: 512               │
                    └────────────┬───────────────────┘
                                 │
                                 ▼
                              ┌──────────────┐
                              │    Answer    │
                              │  (Chinese)   │
                              └──────────────┘
```

## Model Locations

### 🎯 Main Agent Model (Most Important)
- **Location**: `RAG/Rag_test.ipynb` - Cell [15], Line 273
- **Current**: `model_name = "./qwen3-0.6b"`
- **Change to**: `model_name = "Qwen/Qwen2.5-1.5B-Instruct"`

### 🔄 Reranker Model
- **Location**: `RAG/Rag_test.ipynb` - Cell [6], Line 118  
- **Current**: `RERANKER_MODEL_PATH = "E:\\RAG\\reranker\\qwen3-reranker"`
- **Change to**: `RERANKER_MODEL_PATH = "BAAI/bge-reranker-base"`

### 🔢 Embedding Model
- **Location**: `RAG/embedding/embediing_flask.ipynb`
- **Current**: Served via Flask API on port 8888
- **Change**: Edit the embedding service notebook

## Data Flow

```
Question → Vector → Search → [Doc1, Doc2, ...] → Rerank → [Best Docs] → Generate → Answer
           ↑         ↑             ↑                  ↑                      ↑
       Embedding   Milvus      Top-K=5           Score>0.9            Agent Model
        Model        DB      Threshold>0.7                           (CHANGE THIS)
```

## Configuration Hierarchy

```
config.json
    ├── models
    │   ├── agent_model ──────────► Main answer generator (Line 273)
    │   ├── reranker_model ───────► Document scorer (Line 118)
    │   └── embedding_service ────► Vector converter (API)
    │
    ├── milvus ───────────────────► Vector database settings
    │
    ├── generation_params ────────► Answer quality controls
    │   ├── max_new_tokens (512)
    │   ├── temperature (0.7)
    │   └── top_p (0.9)
    │
    └── retrieval_params ─────────► Document selection
        ├── top_k (5)
        ├── similarity_threshold (0.7)
        └── reranker_threshold (0.9)
```

## How Each Model Is Loaded

### Agent Model (Cell 15)
```python
model_name = "./qwen3-0.6b"              # ◄── CHANGE THIS
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)
```

### Reranker Model (Cell 6)
```python
RERANKER_MODEL_PATH = "E:\\RAG\\reranker\\qwen3-reranker"  # ◄── CHANGE THIS
tokenizer = AutoTokenizer.from_pretrained(RERANKER_MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(RERANKER_MODEL_PATH)
```

### Embedding Model (API Call, Cell 3)
```python
url = 'http://127.0.0.1:8888/embed'      # ◄── Service endpoint
response = requests.post(url, json=data)
```

## Quick Change Guide

Want to change the agent model? **Only 1 line needs to change:**

```python
# In RAG/Rag_test.ipynb, Cell [15], Line 273
# From:
model_name = "./qwen3-0.6b"

# To:
model_name = "Qwen/Qwen2.5-1.5B-Instruct"  # Better quality, 4GB RAM
```

That's it! Restart kernel and run all cells.

## System Requirements

```
Component          Model                    RAM      Speed
─────────────────  ─────────────────────    ─────    ─────
Agent (Current)    qwen3-0.6b              2GB      Fast
Agent (Better)     Qwen2.5-1.5B-Instruct   4GB      Medium  ◄── Recommended
Agent (Best)       Qwen2.5-3B-Instruct     8GB      Slower

Reranker          qwen3-reranker           1GB      Fast
Embedding         qwen3-embedding          1GB      Fast

TOTAL (Current)   ~4GB
TOTAL (Better)    ~6GB  ◄── Recommended
TOTAL (Best)      ~10GB
```

## Testing Flow

```
1. Edit config.json OR notebook cell
         ↓
2. Restart Jupyter kernel
         ↓
3. Run all cells (Ctrl+A, Shift+Enter)
         ↓
4. Check answer quality
         ↓
5. Adjust parameters if needed
         ↓
6. Done! ✅
```

---

**Key Takeaway**: The most important model to change is the **Agent Model** in cell [15]. This controls answer quality.
