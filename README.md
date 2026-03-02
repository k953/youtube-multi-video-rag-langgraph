# LangGraph Multi-Video RAG Chatbot


<pre class="overflow-visible! px-0!" data-start="131" data-end="1017"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼ5 ͼj"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span># 🚀 LangGraph Multi-Video RAG Chatbot (YouTube)</span><br/><br/><span>A production-ready **Multi-Video Retrieval Augmented Generation (RAG)** chatbot built with:</span><br/><br/><span>- 🧠 LangGraph (agent workflow)</span><br/><span>- 🔎 FAISS vector search</span><br/><span>- 🤖 OpenAI / GPT (LLM answers)</span><br/><span>- 📺 YouTube auto transcript ingestion</span><br/><span>- ⏱️ Timestamp citations</span><br/><span>- 🧵 Chat memory</span><br/><span>- ⚡ Streamlit UI with token streaming</span><br/><br/><span>Ask questions across multiple YouTube videos and get **context-grounded answers with source timestamps**.</span><br/><br/><span>---</span><br/><br/><span># 🧱 Architecture</span><br/><br/><span>User Question → LangGraph Agent → FAISS Retriever → YouTube Transcript Chunks → GPT Answer → Streamlit UI</span><br/><br/><span>---</span><br/><br/><span># ✨ Features</span><br/><br/><span>✅ Multi-video RAG  </span><br/><span>✅ YouTube transcript auto-ingestion  </span><br/><span>✅ Semantic chunk search (FAISS)  </span><br/><span>✅ Timestamp source citations  </span><br/><span>✅ Chat history memory  </span><br/><span>✅ Streaming tokens UI  </span><br/><span>✅ MCP tool-based retrieval  </span><br/><span>✅ LangGraph stateful workflow  </span><br/><br/><span>---</span><br/><br/><span># 📂 Project Structure</span><br/></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

MCP_RAG_LANGGRAPH/

│

├── agent/

│   └── langgraph_agent.py      # LangGraph workflow

│

├── rag/

│   ├── faiss_store.py          # FAISS index builder

│   └── retriever.py            # Semantic search

│

├── mcp_server/

│   ├── server.py               # MCP search API

│   └── tools.py                # Retrieval tools

│

├── ingest_youtube.py           # YouTube transcript ingestion

├── streamlit_app.py            # Streamlit UI

├── app.py                      # CLI chatbot

├── requirements.txt

└── README.md

<pre class="overflow-visible! px-0!" data-start="1528" data-end="1696"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼ5 ͼj"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><br/><span>---</span><br/><br/><span># ⚙️ Installation</span><br/><br/><span>## 1️⃣ Clone repo</span><br/><br/><span>```bash</span><br/><span>git clone https://github.com/k953/youtube-multi-video-rag-langgraph.git</span><br/><span>cd youtube-multi-video-rag-langgraph</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

## 2️⃣ Create virtual environment

<pre class="overflow-visible! px-0!" data-start="1738" data-end="1847"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼ5 ͼj"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>python </span><span class="ͼf">-m</span><span> venv venv</span><br/><span class="ͼd">source</span><span> venv/bin/activate   </span><span class="ͼ6"># Linux / Mac</span><br/><span>venv\Scripts\activate      </span><span class="ͼ6"># Windows</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

## 3️⃣ Install dependencies

<pre class="overflow-visible! px-0!" data-start="1883" data-end="1926"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼ5 ͼj"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>pip install </span><span class="ͼf">-r</span><span> requirements.txt</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

## 4️⃣ Add OpenAI API Key

Create `.env` file:

<pre class="overflow-visible! px-0!" data-start="1981" data-end="2020"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼ5 ͼj"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>OPENAI_API_KEY=your_key_here</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

# 📺 Ingest YouTube Videos

<pre class="overflow-visible! px-0!" data-start="2055" data-end="2091"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼ5 ͼj"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>python ingest_youtube.py</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

Add multiple YouTube URLs inside the script → transcripts will be chunked and indexed in FAISS.

---

# 🖥️ Run MCP Server

<pre class="overflow-visible! px-0!" data-start="2217" data-end="2279"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼ5 ͼj"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>uvicorn mcp_server.server:app </span><span class="ͼf">--reload</span><span></span><span class="ͼf">--port</span><span></span><span class="ͼb">8000</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

# 💬 Run CLI Chatbot

<pre class="overflow-visible! px-0!" data-start="2308" data-end="2333"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼ5 ͼj"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>python app.py</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

# 🌐 Run Streamlit UI

<pre class="overflow-visible! px-0!" data-start="2363" data-end="2405"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼ5 ͼj"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>streamlit run streamlit_app.py</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

# 🧠 Example Query

> What does the video say about neural networks?

✔ Returns grounded answer

✔ Shows timestamp citations

✔ Uses multi-video context

---

# 🔗 Tech Stack

* LangGraph
* OpenAI GPT-4 / GPT-4o
* FAISS
* FastAPI (MCP server)
* Streamlit
* YouTube Transcript API
* Python

---

# 📊 Use Cases

* 🎓 Lecture Q&A across multiple videos
* 🧪 Research assistant for video content
* 🏢 Knowledge base from internal recordings
* 📚 Course revision chatbot

---

# 🚀 Future Improvements

* Vector DB (Pinecone / Weaviate)
* Hybrid search (BM25 + embeddings)
* Whisper for audio ingestion
* Docker deployment
* Auth + multi-user memory
