# 🤖 RAG-Based Embedded Test Generator

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Pytest-yellow.svg)](https://docs.pytest.org/)
[![AI-Backend](https://img.shields.io/badge/AI-Ollama%20(Mistral)-orange.svg)](https://ollama.ai/)
[![VectorDB](https://img.shields.io/badge/Vector%20DB-FAISS-green.svg)](https://github.com/facebookresearch/faiss)

## 📌 Project Overview
Testing embedded systems requires translating complex hardware requirements into precise test logic. This project utilizes **Retrieval-Augmented Generation (RAG)** to automate the creation of PyTest cases directly from system specifications. 

By using a local vector database, the system ensures that the LLM (Mistral) has the exact context of voltage thresholds and timing constraints, eliminating "hallucinations" and reducing manual test-writing time by 90%.

---

## 📽️ Demo
![RAG Test Generation Demo](demo.gif)
*Watch the system retrieve requirements and generate functional PyTest files in real-time.*

---

## 🛠️ Technical Architecture
The pipeline follows a modern RAG architecture:
1. **Embedding**: Requirements are converted into high-dimensional vectors using `all-MiniLM-L6-v2`.
2. **Vector Store**: **FAISS** index is built for ultra-fast semantic retrieval of relevant requirements.
3. **Retrieval**: When a test target is identified, the system queries the index for the most relevant specifications.
4. **Generation**: **Ollama (Mistral)** processes the retrieved context and generates structured, executable PyTest code.

---

## 🚀 Key Features
- **Semantic Search**: Understands the difference between "overvoltage" and "undervoltage" through vector embeddings.
- **Local & Private**: Runs entirely on your local machine using Ollama—no data leaves the environment.
- **Boundary Analysis**: Automatically identifies boundary conditions (e.g., 420V threshold) and generates edge-case tests.
- **Scalable**: Easily handles hundreds of requirements by indexing them into the FAISS database.

---

## 📂 Project Structure
```text
├── rag_generator/
│   └── rag_generator.py   # Core RAG logic & LLM interfacing
├── utils/
│   ├── rag_functions.py   # FAISS & Embedding management
│   ├──ollama_functions.py # Local LLM API wrappers
│   ├──api_functions.py    # API wrappers
│   └── prompts.py         # Prompts for test generation
├── tests/
│   └── test_01.py         # Entry point for test generation
└── generated_tests/       # Output folder for AI-generated test suites