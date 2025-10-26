"""
Example script showing how to change models in the RAG system.
This demonstrates different ways to update model configurations.
"""

from config_loader import RAGConfig

def example_change_to_larger_model():
    """Example: Switch to a larger Qwen model for better quality."""
    print("Example 1: Changing to Qwen2.5-1.5B-Instruct")
    print("-" * 50)
    
    config = RAGConfig()
    
    # Option A: Use a local model path
    # config.update_agent_model("./RAG/qwen2.5-1.5b")
    
    # Option B: Use HuggingFace model directly (recommended)
    config.update_agent_model("Qwen/Qwen2.5-1.5B-Instruct")
    
    print(f"✓ Agent model updated to: {config.get_agent_model_path()}")
    print("\nNext steps:")
    print("1. Open RAG/Rag_test.ipynb")
    print("2. In cell [15], change model_name to match the new path")
    print("3. Run all cells to test the new model")
    print()


def example_change_to_llama():
    """Example: Switch to Llama model."""
    print("Example 2: Changing to Llama-3.2-1B-Instruct")
    print("-" * 50)
    
    config = RAGConfig()
    config.update_agent_model("meta-llama/Llama-3.2-1B-Instruct")
    
    print(f"✓ Agent model updated to: {config.get_agent_model_path()}")
    print("\nNote: Llama models may require authentication on HuggingFace")
    print("Run: huggingface-cli login")
    print()


def example_change_reranker():
    """Example: Switch to a different reranker model."""
    print("Example 3: Changing to BGE reranker")
    print("-" * 50)
    
    config = RAGConfig()
    config.update_reranker_model("BAAI/bge-reranker-base")
    
    print(f"✓ Reranker model updated to: {config.get_reranker_model_path()}")
    print("\nNext steps:")
    print("1. Open RAG/Rag_test.ipynb")
    print("2. In cell [6], update RERANKER_MODEL_PATH")
    print("3. You may need to adjust the scoring logic for different reranker models")
    print()


def example_view_current_config():
    """Example: View current configuration."""
    print("Current RAG System Configuration")
    print("=" * 50)
    
    config = RAGConfig()
    
    print("\n📦 Models:")
    print(f"  Agent Model: {config.get_agent_model_path()}")
    print(f"  Reranker Model: {config.get_reranker_model_path()}")
    print(f"  Embedding Model: {config.get_embedding_model_path()}")
    
    print("\n🔗 Services:")
    print(f"  Embedding Service: {config.get_embedding_service_url()}")
    
    milvus = config.get_milvus_config()
    print(f"\n💾 Milvus Database:")
    print(f"  URL: {milvus['url']}")
    print(f"  Database: {milvus['db_name']}")
    print(f"  Collection: {milvus['collection_name']}")
    
    gen_params = config.get_generation_params()
    print(f"\n⚙️  Generation Parameters:")
    print(f"  Max Tokens: {gen_params['max_new_tokens']}")
    print(f"  Temperature: {gen_params['temperature']}")
    print(f"  Top-p: {gen_params['top_p']}")
    
    ret_params = config.get_retrieval_params()
    print(f"\n🔍 Retrieval Parameters:")
    print(f"  Top-k: {ret_params['top_k']}")
    print(f"  Similarity Threshold: {ret_params['similarity_threshold']}")
    print(f"  Reranker Threshold: {ret_params['reranker_threshold']}")
    print()


def example_quick_start():
    """Quick start guide for changing models."""
    print("\n" + "=" * 60)
    print("QUICK START: How to Change Your Model")
    print("=" * 60)
    print()
    print("Step 1: Choose Your Model")
    print("  - Qwen/Qwen2.5-1.5B-Instruct (Recommended for balance)")
    print("  - Qwen/Qwen2.5-3B-Instruct (Better quality, needs more RAM)")
    print("  - meta-llama/Llama-3.2-1B-Instruct (Alternative)")
    print()
    print("Step 2: Update Configuration")
    print("  Method A - Edit config.json manually:")
    print('    Change "agent_model" -> "path" to your model name')
    print()
    print("  Method B - Use this script:")
    print("    from config_loader import RAGConfig")
    print('    config = RAGConfig()')
    print('    config.update_agent_model("Qwen/Qwen2.5-1.5B-Instruct")')
    print()
    print("Step 3: Update the Notebook")
    print("  Open RAG/Rag_test.ipynb, Cell [15]:")
    print('    model_name = "Qwen/Qwen2.5-1.5B-Instruct"')
    print()
    print("Step 4: Test Your Changes")
    print("  Run all cells in RAG/Rag_test.ipynb")
    print()
    print("=" * 60)
    print()


if __name__ == "__main__":
    # Show quick start guide
    example_quick_start()
    
    # View current configuration
    example_view_current_config()
    
    # Uncomment the example you want to try:
    
    # example_change_to_larger_model()
    # example_change_to_llama()
    # example_change_reranker()
    
    print("\n💡 Tip: Uncomment the examples above to try different configurations!")
    print("Run: python examples_change_model.py")
