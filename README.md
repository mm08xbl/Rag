# RAG (Retrieval-Augmented Generation) System

A Chinese banking intelligent customer service system built with Retrieval-Augmented Generation (RAG) technology, featuring document retrieval, reranking, and answer generation capabilities.

## System Architecture

The system consists of three main models:

1. **Agent Model (Answer Generation)**: Generates responses based on retrieved documents
2. **Reranker Model**: Scores and ranks document relevance  
3. **Embedding Model**: Converts text into vector embeddings for similarity search

## How to Change the Model in Agent

### Quick Start

The easiest way to change models is to edit the `config.json` file in the root directory:

```json
{
  "models": {
    "agent_model": {
      "path": "./RAG/qwen3-0.6b",
      ...
    }
  }
}
```

### Method 1: Change the Agent Model (Recommended)

The agent model is responsible for generating final answers. To change it:

#### Option A: Using a Local Model

1. **Download your preferred model**  
   Download a compatible Hugging Face model to your local system. Example models:
   - `Qwen/Qwen2.5-1.5B-Instruct` (larger, more accurate)
   - `Qwen/Qwen2.5-3B-Instruct` (even better quality)
   - `meta-llama/Llama-3.2-1B-Instruct`
   - Any other causal language model compatible with transformers

2. **Update the configuration**  
   Edit `config.json`:
   ```json
   {
     "models": {
       "agent_model": {
         "path": "./RAG/your-new-model-folder"
       }
     }
   }
   ```

3. **Update the notebook**  
   Open `RAG/Rag_test.ipynb` and modify cell [15]:
   ```python
   # Change this line:
   model_name = "./qwen3-0.6b"
   
   # To:
   model_name = "./your-new-model-folder"
   # Or use absolute path:
   model_name = "/path/to/your/model"
   ```

#### Option B: Using Hugging Face Hub Directly

Instead of downloading the model, you can load it directly from Hugging Face:

```python
# In Rag_test.ipynb, cell [15]:
model_name = "Qwen/Qwen2.5-1.5B-Instruct"  # Or any HF model name
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)
```

### Method 2: Change the Reranker Model

The reranker model scores document relevance. To change it:

1. **Download a reranker model**  
   Compatible models:
   - `BAAI/bge-reranker-base`
   - `BAAI/bge-reranker-large`  
   - `cross-encoder/ms-marco-MiniLM-L-12-v2`

2. **Update the notebook**  
   Open `RAG/Rag_test.ipynb` and modify cell [6]:
   ```python
   # Change this line:
   RERANKER_MODEL_PATH = "E:\\RAG\\reranker\\qwen3-reranker"
   
   # To:
   RERANKER_MODEL_PATH = "./RAG/reranker/your-new-reranker"
   # Or use HuggingFace model:
   RERANKER_MODEL_PATH = "BAAI/bge-reranker-base"
   ```

### Method 3: Change the Embedding Model

The embedding model is served via a Flask API. To change it:

1. **Update the embedding service**  
   The embedding service is defined in `RAG/embedding/embediing_flask.ipynb`
   
2. **Modify the model path**  
   In the embedding service notebook, change the model path to your preferred embedding model:
   ```python
   model_path = "./qwen3-embedding"
   # Change to:
   model_path = "BAAI/bge-base-zh-v1.5"  # Or your preferred embedding model
   ```

3. **Restart the embedding service**  
   After making changes, restart the embedding service to apply the new model.

## Model Requirements

### Agent Model Requirements
- Must be compatible with Hugging Face `AutoModelForCausalLM`
- Should support Chinese language for this use case
- Recommended: Instruction-tuned models
- Minimum: 0.5B parameters, Recommended: 1.5B-7B parameters

### Reranker Model Requirements  
- Should output binary classification (yes/no) or relevance scores
- Compatible with the custom scoring logic in the notebook
- Recommended: Cross-encoder models trained for semantic similarity

### Embedding Model Requirements
- Must output fixed-size vector embeddings (typically 768 or 1024 dimensions)
- Should be compatible with Milvus vector database
- Recommended: Models trained on Chinese text for this use case

## Configuration Parameters

Edit `config.json` to customize:

```json
{
  "generation_params": {
    "max_new_tokens": 512,    // Maximum length of generated response
    "temperature": 0.7,        // Creativity (0.0-1.0)
    "top_p": 0.9              // Nucleus sampling
  },
  "retrieval_params": {
    "top_k": 5,                      // Number of documents to retrieve
    "similarity_threshold": 0.7,      // Minimum similarity score
    "reranker_threshold": 0.9         // Minimum reranker score
  }
}
```

## Testing Your Model Changes

After changing models, run the test in `Rag_test.ipynb`:

1. Ensure all services are running:
   - Milvus vector database (port 19530)
   - Embedding service (port 8888)

2. Execute all cells in the notebook

3. Check the output quality in the final cell

4. Adjust parameters in `config.json` if needed

## Troubleshooting

### Model Loading Errors
- **Error**: "OSError: Model not found"
  - **Solution**: Verify the model path is correct
  - **Solution**: Ensure the model is downloaded completely

### Out of Memory Errors  
- **Solution**: Use a smaller model (e.g., 0.5B instead of 3B)
- **Solution**: Reduce `max_new_tokens` in config
- **Solution**: Enable model quantization:
  ```python
  model = AutoModelForCausalLM.from_pretrained(
      model_name, 
      trust_remote_code=True,
      load_in_8bit=True  # Enable 8-bit quantization
  )
  ```

### Poor Answer Quality
- **Solution**: Try a larger model
- **Solution**: Adjust `temperature` (lower = more focused, higher = more creative)
- **Solution**: Increase `top_k` to retrieve more documents
- **Solution**: Lower `similarity_threshold` to get more candidate documents

## Performance Comparison

| Model | Size | Speed | Quality | Memory |
|-------|------|-------|---------|--------|
| Qwen2.5-0.5B | 0.5B | Fast | Good | 2GB |
| Qwen2.5-1.5B | 1.5B | Medium | Better | 4GB |
| Qwen2.5-3B | 3B | Slower | Best | 8GB |
| Qwen2.5-7B | 7B | Slow | Excellent | 16GB |

## Additional Resources

- [Qwen Models on Hugging Face](https://huggingface.co/Qwen)
- [BGE Embedding Models](https://huggingface.co/BAAI)
- [Transformers Documentation](https://huggingface.co/docs/transformers)

## License

Please refer to the individual model licenses when using different models.
