from rag.retriever import search_vector

def search_transcript(query: str):
    results = search_vector(query)
    return {"results": results}