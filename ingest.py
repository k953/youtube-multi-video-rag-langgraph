from youtube_transcript_api import YouTubeTranscriptApi
from rag.faiss_store import create_vector_store

VIDEO_ID = "dQw4w9WgXcQ"  # 👈 change karo

def get_transcript(video_id):
    transcript = YouTubeTranscriptApi().fetch(video_id)
    text = " ".join([t.text for t in transcript])
    return text

def chunk_text(text, chunk_size=500):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

if __name__ == "__main__":
    print("Fetching transcript...")
    text = get_transcript(VIDEO_ID)

    print("Chunking text...")
    chunks = chunk_text(text)

    print("Creating FAISS index...")
    create_vector_store(chunks)

    print("✅ FAISS index created successfully!")