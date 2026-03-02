from youtube_transcript_api import YouTubeTranscriptApi
from rag.faiss_store import add_chunks

def ingest_youtube(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    chunks = []
    for t in transcript:
        text = t["text"]
        start = int(t["start"])
        ts = f"{start//60:02}:{start%60:02}"

        chunks.append({
            "text": text,
            "timestamp": ts,
            "video_id": video_id
        })

    add_chunks(chunks)
    print(f"✅ Ingested video: {video_id}")