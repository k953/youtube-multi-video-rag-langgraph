def search(query, video_id=None, k=5):
    docs = vectorstore.similarity_search(query, k=k)

    if video_id:
        docs = [d for d in docs if d.metadata["video_id"] == video_id]

    results = []
    for d in docs:
        results.append({
            "text": d.page_content,
            "timestamp": d.metadata["timestamp"],
            "video_id": d.metadata["video_id"]
        })

    return results