"""
Configuration loader for RAG system.
This module provides easy access to model configurations.
"""

import json
import os
from pathlib import Path

class RAGConfig:
    """Load and manage RAG system configuration."""
    
    def __init__(self, config_path="config.json"):
        """
        Initialize configuration loader.
        
        Args:
            config_path: Path to config.json file
        """
        self.config_path = Path(config_path)
        self.config = self._load_config()
    
    def _load_config(self):
        """Load configuration from JSON file."""
        if not self.config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {self.config_path}\n"
                f"Please create a config.json file or specify the correct path."
            )
        
        with open(self.config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def get_agent_model_path(self):
        """Get the path to the agent/answer generation model."""
        return self.config['models']['agent_model']['path']
    
    def get_reranker_model_path(self):
        """Get the path to the reranker model."""
        return self.config['models']['reranker_model']['path']
    
    def get_embedding_service_url(self):
        """Get the URL for the embedding service."""
        return self.config['models']['embedding_service']['url']
    
    def get_embedding_model_path(self):
        """Get the path to the embedding model."""
        return self.config['models']['embedding_service']['model_path']
    
    def get_milvus_config(self):
        """Get Milvus database configuration."""
        return self.config['milvus']
    
    def get_generation_params(self):
        """Get text generation parameters."""
        return self.config['generation_params']
    
    def get_retrieval_params(self):
        """Get document retrieval parameters."""
        return self.config['retrieval_params']
    
    def update_agent_model(self, new_path):
        """
        Update the agent model path in configuration.
        
        Args:
            new_path: New path to the agent model
        """
        self.config['models']['agent_model']['path'] = new_path
        self._save_config()
    
    def update_reranker_model(self, new_path):
        """
        Update the reranker model path in configuration.
        
        Args:
            new_path: New path to the reranker model
        """
        self.config['models']['reranker_model']['path'] = new_path
        self._save_config()
    
    def _save_config(self):
        """Save configuration back to JSON file."""
        with open(self.config_path, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)


# Example usage
if __name__ == "__main__":
    # Load configuration
    config = RAGConfig()
    
    # Print current configuration
    print("Current Configuration:")
    print(f"Agent Model: {config.get_agent_model_path()}")
    print(f"Reranker Model: {config.get_reranker_model_path()}")
    print(f"Embedding Service: {config.get_embedding_service_url()}")
    print(f"Milvus: {config.get_milvus_config()}")
    print(f"Generation Params: {config.get_generation_params()}")
    print(f"Retrieval Params: {config.get_retrieval_params()}")
    
    # Example: Update agent model
    # config.update_agent_model("./RAG/qwen3-1.5b")
    # print(f"\nUpdated Agent Model: {config.get_agent_model_path()}")
