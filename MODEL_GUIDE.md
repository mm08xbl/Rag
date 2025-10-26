# Model Configuration Guide

## Quick Reference: Changing Models

### Current Model Locations in Code

The RAG system uses three models:

1. **Agent Model (Answer Generation)** - Line 273 in `RAG/Rag_test.ipynb`:
   ```python
   model_name = "./qwen3-0.6b"
   ```

2. **Reranker Model** - Line 118 in `RAG/Rag_test.ipynb`:
   ```python
   RERANKER_MODEL_PATH = "E:\\RAG\\reranker\\qwen3-reranker"
   ```

3. **Embedding Model** - Accessed via API at line 41:
   ```python
   url = 'http://127.0.0.1:8888/embed'
   ```

## How to Change Models

### Method 1: Direct Edit (Simplest)

Edit `RAG/Rag_test.ipynb` directly:

**For Agent Model (Cell 15):**
```python
# Original:
model_name = "./qwen3-0.6b"

# Change to larger model:
model_name = "Qwen/Qwen2.5-1.5B-Instruct"

# Or use local path:
model_name = "./qwen2.5-1.5b"
```

**For Reranker Model (Cell 6):**
```python
# Original:
RERANKER_MODEL_PATH = "E:\\RAG\\reranker\\qwen3-reranker"

# Change to:
RERANKER_MODEL_PATH = "BAAI/bge-reranker-base"
```

### Method 2: Use Configuration File

1. Edit `config.json`:
   ```json
   {
     "models": {
       "agent_model": {
         "path": "Qwen/Qwen2.5-1.5B-Instruct"
       }
     }
   }
   ```

2. Add this cell at the beginning of `Rag_test.ipynb`:
   ```python
   from config_loader import RAGConfig
   config = RAGConfig()
   
   # Use config values
   model_name = config.get_agent_model_path()
   RERANKER_MODEL_PATH = config.get_reranker_model_path()
   ```

### Method 3: Use Helper Script

```bash
python examples_change_model.py
```

This shows current config and provides examples for changing models.

## Recommended Models

### For Agent (Answer Generation)

| Model | Parameters | Memory | Quality | Speed |
|-------|-----------|---------|---------|-------|
| Qwen/Qwen2.5-0.5B-Instruct | 0.5B | ~2GB | Good | Fast |
| Qwen/Qwen2.5-1.5B-Instruct | 1.5B | ~4GB | Better | Medium |
| Qwen/Qwen2.5-3B-Instruct | 3B | ~8GB | Best | Slower |
| meta-llama/Llama-3.2-1B | 1B | ~3GB | Good | Medium |

### For Reranker

- `BAAI/bge-reranker-base` - Good balance
- `BAAI/bge-reranker-large` - Better quality
- `cross-encoder/ms-marco-MiniLM-L-12-v2` - Faster

### For Embedding

- `BAAI/bge-base-zh-v1.5` - Chinese optimized
- `sentence-transformers/paraphrase-multilingual-mpnet-base-v2` - Multilingual

## Testing After Changes

1. Restart Jupyter kernel
2. Run all cells in `Rag_test.ipynb`
3. Check the answer quality in the final cell
4. Adjust generation parameters in `config.json` if needed

## Troubleshooting

**"Model not found"**
- Check internet connection (for HuggingFace models)
- Verify model path is correct
- Try: `huggingface-cli download <model-name>`

**"Out of memory"**
- Use a smaller model
- Enable quantization:
  ```python
  model = AutoModelForCausalLM.from_pretrained(
      model_name,
      load_in_8bit=True
  )
  ```

**"Poor answer quality"**
- Try a larger model
- Adjust temperature in `config.json` (0.3-0.7 for more focused answers)
- Increase top_k to retrieve more documents

## Example Workflow

```bash
# 1. View current configuration
python examples_change_model.py

# 2. Update to a better model
python -c "from config_loader import RAGConfig; RAGConfig().update_agent_model('Qwen/Qwen2.5-1.5B-Instruct')"

# 3. Update notebook cell [15] to use new model
# 4. Run all cells in Rag_test.ipynb
# 5. Enjoy better results!
```
