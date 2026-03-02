import streamlit as st
from openai import OpenAI
from agent.langgraph_agent import app_graph

client = OpenAI()

st.title("🎬 Video RAG Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

query = st.text_input("Ask question about video")

if st.button("Ask") and query:
    placeholder = st.empty()

    state = {
        "query": query,
        "chat_history": st.session_state.history
    }

    result = app_graph.invoke(state)

    # streaming simulation (LLM already done)
    answer = result["answer"]

    streamed = ""
    for token in answer.split():
        streamed += token + " "
        placeholder.markdown(streamed)
        st.sleep(0.02)

    st.session_state.history.append(f"User: {query}")
    st.session_state.history.append(f"Assistant: {answer}")

st.markdown("### 🧠 Chat Memory")
for msg in st.session_state.history:
    st.write(msg)