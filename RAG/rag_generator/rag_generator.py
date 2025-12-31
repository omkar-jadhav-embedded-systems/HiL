import os
import sys
from utils.ollama_functions import check_ollama_running , pull_model
from utils.rag_functions import retrieve_context, build_rag_index
from utils.api_functions import generate_test_rag
from dotenv import load_dotenv

load_dotenv()

MODEL = os.getenv("MODEL")

def rag_test_generator(REQUIREMENTS):
    print("\n=== RAG-Based Embedded Test Generator ===\n")

    if not check_ollama_running():
        print("Start Ollama first using: ollama serve")
        sys.exit(1)

    pull_model(MODEL)

    # Build RAG
    index, embedder, texts, keys = build_rag_index(REQUIREMENTS)

    # Generate tests
    for test_intent in REQUIREMENTS.keys():
        context = retrieve_context(
            query=test_intent,
            index=index,
            embedder=embedder,
            texts=texts
        )

        generate_test_rag(test_intent, context)

    print("\n🎯 All tests generated successfully")