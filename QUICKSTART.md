# Quick Start: Changing Models in RAG System

## 🎯 What You Asked: "How can I change your model in agent?"

### Answer: Here are 3 simple methods to change the model:

---

## Method 1: Edit config.json (Easiest) ✅

1. Open `config.json`
2. Find this section:
```json
"agent_model": {
  "path": "./RAG/qwen3-0.6b"
}
```

3. Change it to your desired model:
```json
"agent_model": {
  "path": "Qwen/Qwen2.5-1.5B-Instruct"
}
```

4. Open `RAG/Rag_test.ipynb`, go to cell [15], and update:
```python
model_name = "Qwen/Qwen2.5-1.5B-Instruct"
```

5. Run all cells - Done! ✨

---

## Method 2: Use Python Script 🐍

Run this command:
```bash
python examples_change_model.py
```

This shows you:
- Current model configuration
- Examples for changing models
- Step-by-step instructions

To change the model programmatically:
```python
from config_loader import RAGConfig

config = RAGConfig()
config.update_agent_model("Qwen/Qwen2.5-1.5B-Instruct")
```

---

## Method 3: Direct Notebook Edit 📓

Open `RAG/Rag_test.ipynb` and find cell [15]:

**Original:**
```python
model_name = "./qwen3-0.6b"
```

**Change to any of these:**
```python
# Option 1: Larger Qwen model (better quality)
model_name = "Qwen/Qwen2.5-1.5B-Instruct"

# Option 2: Even better quality (needs more RAM)
model_name = "Qwen/Qwen2.5-3B-Instruct"

# Option 3: Llama model
model_name = "meta-llama/Llama-3.2-1B-Instruct"

# Option 4: Local model path
model_name = "./RAG/my-custom-model"
```

---

## 📊 Model Recommendations

| Model | Best For | Memory | Quality |
|-------|----------|---------|---------|
| `Qwen/Qwen2.5-0.5B-Instruct` | Testing, low RAM | 2GB | Good |
| `Qwen/Qwen2.5-1.5B-Instruct` | **Recommended** | 4GB | Better |
| `Qwen/Qwen2.5-3B-Instruct` | Best quality | 8GB | Excellent |
| `meta-llama/Llama-3.2-1B` | Alternative | 3GB | Good |

---

## 🔧 What About Other Models?

### Reranker Model
Change line 118 in `RAG/Rag_test.ipynb`:
```python
RERANKER_MODEL_PATH = "BAAI/bge-reranker-base"
```

### Embedding Model  
The embedding model runs as a service. To change it:
1. Open `RAG/embedding/embediing_flask.ipynb`
2. Change the model path in that notebook
3. Restart the embedding service

---

## ✅ Testing Your Changes

After changing the model:

1. **Restart Jupyter kernel** (Important!)
2. **Run all cells** in `RAG/Rag_test.ipynb`
3. **Check the output** in the last cell
4. **Adjust parameters** in `config.json` if needed

---

## 🆘 Troubleshooting

**"Model not found"**
```bash
# Install huggingface-cli and login
pip install huggingface-hub
huggingface-cli login
```

**"Out of memory"**
- Use smaller model (0.5B instead of 3B)
- Enable quantization in notebook cell [15]:
```python
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    trust_remote_code=True,
    load_in_8bit=True  # Add this line
)
```

**"Answers are not good"**
- Try larger model (1.5B or 3B)
- Edit `config.json` and lower temperature:
```json
"temperature": 0.3  // More focused answers
```

---

## 📚 More Information

- `README.md` - Complete documentation
- `MODEL_GUIDE.md` - Detailed model guide
- `config.json` - All configuration options
- `examples_change_model.py` - Interactive examples

---

## 💡 Pro Tips

1. **Start with `Qwen/Qwen2.5-1.5B-Instruct`** - Good balance of quality and speed
2. **Always restart Jupyter kernel** after changing models
3. **Use HuggingFace model names** instead of downloading (e.g., `Qwen/Qwen2.5-1.5B-Instruct`)
4. **Adjust temperature** in config.json to control answer creativity
5. **Monitor memory usage** - larger models need more RAM

---

**That's it! You now know how to change the model in your RAG agent.** 🎉

For questions, check `README.md` or run:
```bash
python examples_change_model.py
```
