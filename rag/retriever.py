from rag.faiss_store import load_vector_store

db = load_vector_store()

def search_vector(query: str, k: int = 3):
    docs = db.similarity_search(query, k=k)
    return [doc.page_content for doc in docs]