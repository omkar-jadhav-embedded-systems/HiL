import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

def build_rag_index(requirements: dict):
    """
    Builds FAISS index from in-file requirements.
    """
    print("🔍 Building FAISS index for requirements...")

    embedder = SentenceTransformer("all-MiniLM-L6-v2")

    texts = list(requirements.values())
    keys = list(requirements.keys())

    embeddings = embedder.encode(texts)
    embeddings = np.array(embeddings).astype("float32")

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    print("✅ RAG index ready")
    return index, embedder, texts, keys


def retrieve_context(query, index, embedder, texts, top_k=1):
    """
    Retrieves most relevant requirement for a query.
    """
    query_vec = embedder.encode([query])
    query_vec = np.array(query_vec).astype("float32")

    distances, indices = index.search(query_vec, top_k)
    return texts[indices[0][0]]
