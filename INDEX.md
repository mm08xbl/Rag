# 📚 Documentation Index

Welcome to the RAG System documentation! This index will help you find the information you need.

## 🚀 Start Here

### New to the project?
1. **[QUICKSTART.md](QUICKSTART.md)** - Answer to "How can I change your model in agent?"
   - 3 simple methods to change models
   - Recommended models
   - Common troubleshooting

### Want to understand the system?
2. **[ARCHITECTURE.md](ARCHITECTURE.md)** - Visual system architecture
   - How the RAG system works
   - Where each model is located
   - Data flow diagram

### Need detailed instructions?
3. **[README.md](README.md)** - Complete system documentation
   - Full setup guide
   - Detailed model requirements
   - Performance comparisons
   - Advanced configurations

### Want a quick reference?
4. **[MODEL_GUIDE.md](MODEL_GUIDE.md)** - Quick reference guide
   - Current model locations in code
   - Testing workflow
   - Troubleshooting tips

## 🛠️ Configuration Files

### For automated setup:
- **[config.json](config.json)** - Central configuration file
  - Model paths
  - Service URLs
  - Generation parameters
  - Retrieval settings

### For programmatic access:
- **[config_loader.py](config_loader.py)** - Python configuration loader
  - Load config.json
  - Update model paths
  - Access all settings
  ```bash
  python config_loader.py  # View current config
  ```

### For learning by example:
- **[examples_change_model.py](examples_change_model.py)** - Interactive examples
  - View current configuration
  - See example model changes
  - Quick start guide
  ```bash
  python examples_change_model.py  # Run examples
  ```

## 📖 Documentation by Topic

### Changing Models
| What you want to do | Read this |
|---------------------|-----------|
| Change the agent model quickly | [QUICKSTART.md](QUICKSTART.md) → Method 1 |
| Understand where models are | [ARCHITECTURE.md](ARCHITECTURE.md) |
| See all available models | [README.md](README.md) → Recommended Models |
| Use Python to change models | [examples_change_model.py](examples_change_model.py) |

### Configuration
| What you want to configure | Read this |
|----------------------------|-----------|
| Model paths | [config.json](config.json) → models section |
| Answer quality (temperature, etc) | [config.json](config.json) → generation_params |
| How many documents to retrieve | [config.json](config.json) → retrieval_params |
| Database settings | [config.json](config.json) → milvus section |

### Troubleshooting
| Problem | Solution Location |
|---------|-------------------|
| Model not found | [QUICKSTART.md](QUICKSTART.md) → Troubleshooting |
| Out of memory | [README.md](README.md) → Troubleshooting |
| Poor answer quality | [MODEL_GUIDE.md](MODEL_GUIDE.md) → Troubleshooting |
| General issues | [README.md](README.md) → Troubleshooting |

### Understanding the System
| Topic | Document |
|-------|----------|
| System architecture | [ARCHITECTURE.md](ARCHITECTURE.md) |
| Data flow | [ARCHITECTURE.md](ARCHITECTURE.md) → Data Flow |
| Model requirements | [README.md](README.md) → Model Requirements |
| Performance comparison | [README.md](README.md) → Performance Comparison |

## 🎯 Quick Navigation by Role

### I'm a Developer
Start with: [README.md](README.md) → [config_loader.py](config_loader.py)
- Understand the full system
- Use Python tools for configuration
- Check [ARCHITECTURE.md](ARCHITECTURE.md) for system design

### I'm a Data Scientist
Start with: [MODEL_GUIDE.md](MODEL_GUIDE.md) → [config.json](config.json)
- See model locations
- Adjust parameters
- Compare model performance in [README.md](README.md)

### I Just Want to Change the Model
Start with: **[QUICKSTART.md](QUICKSTART.md)**
- Follow Method 1
- Takes 2 minutes
- No coding needed

### I Want to Experiment
Start with: [examples_change_model.py](examples_change_model.py) → [config.json](config.json)
- Run examples
- Edit config.json
- Test different models

## 📝 File Overview

```
.
├── QUICKSTART.md              # ⭐ START HERE - Quick answer to changing models
├── README.md                  # 📖 Complete documentation
├── ARCHITECTURE.md            # 🏗️  System architecture diagrams
├── MODEL_GUIDE.md             # 📚 Quick reference guide
├── INDEX.md                   # 📑 This file
│
├── config.json                # ⚙️  Central configuration
├── config_loader.py           # 🐍 Python config loader
├── examples_change_model.py   # 💡 Interactive examples
│
├── .gitignore                 # 🚫 Git ignore patterns
│
└── RAG/                       # 📁 Main application code
    ├── Rag_test.ipynb        # 🎯 Main notebook (change models here)
    ├── embedding/             # Vector embedding service
    ├── milvus/                # Vector database
    ├── pdf2text/              # Document processing
    └── qwen3-0.6b/            # Default model files
```

## 🎓 Learning Path

### Beginner
1. Read [QUICKSTART.md](QUICKSTART.md)
2. Follow Method 1 to change a model
3. Test the change
4. ✅ You're done!

### Intermediate
1. Read [ARCHITECTURE.md](ARCHITECTURE.md)
2. Read [MODEL_GUIDE.md](MODEL_GUIDE.md)
3. Experiment with [examples_change_model.py](examples_change_model.py)
4. Edit [config.json](config.json)
5. Try different models

### Advanced
1. Read [README.md](README.md) completely
2. Understand [ARCHITECTURE.md](ARCHITECTURE.md)
3. Use [config_loader.py](config_loader.py) programmatically
4. Modify notebooks for your use case
5. Adjust all parameters in [config.json](config.json)
6. Optimize for your specific needs

## ❓ Common Questions

**Q: How do I change the model?**
A: See [QUICKSTART.md](QUICKSTART.md) - Method 1 is the easiest.

**Q: Which model should I use?**
A: `Qwen/Qwen2.5-1.5B-Instruct` - see [README.md](README.md) for details.

**Q: Where is the model loaded in the code?**
A: See [ARCHITECTURE.md](ARCHITECTURE.md) → Model Locations.

**Q: How do I configure parameters?**
A: Edit [config.json](config.json) - see [README.md](README.md) → Configuration Parameters.

**Q: Something broke, what do I do?**
A: Check [QUICKSTART.md](QUICKSTART.md) → Troubleshooting, then [README.md](README.md) → Troubleshooting.

**Q: Can I use this programmatically?**
A: Yes! See [config_loader.py](config_loader.py) and [examples_change_model.py](examples_change_model.py).

## 🔗 External Resources

- [Qwen Models](https://huggingface.co/Qwen) - Available Qwen models
- [HuggingFace Transformers](https://huggingface.co/docs/transformers) - Library documentation
- [Milvus Documentation](https://milvus.io/docs) - Vector database docs

## 📞 Need Help?

1. Check the troubleshooting sections in:
   - [QUICKSTART.md](QUICKSTART.md)
   - [MODEL_GUIDE.md](MODEL_GUIDE.md)
   - [README.md](README.md)

2. Run the examples:
   ```bash
   python examples_change_model.py
   ```

3. Check your configuration:
   ```bash
   python config_loader.py
   ```

## 🎉 Success Stories

After following these docs, you should be able to:
- ✅ Change the agent model in 2 minutes
- ✅ Understand the system architecture
- ✅ Configure all parameters
- ✅ Troubleshoot common issues
- ✅ Optimize for your use case

---

**Remember**: The main model to change is the **Agent Model** in `RAG/Rag_test.ipynb` cell [15].
For the quickest answer, go to **[QUICKSTART.md](QUICKSTART.md)**.
