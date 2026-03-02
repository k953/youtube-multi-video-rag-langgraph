from fastapi import FastAPI
from mcp_server.tools import search_transcript

app = FastAPI()

@app.get("/search")
def search(query: str):
    return search_transcript(query)