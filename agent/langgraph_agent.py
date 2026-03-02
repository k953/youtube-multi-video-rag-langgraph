from langgraph.graph import StateGraph, END
import requests

class AgentState(dict):
    pass

# 🔹 Node 1 — Planner
# 🔹 Node 1 — Planner
def planner(state: AgentState):
    return state

# 🔹 Node 2 — MCP Tool Call
def tool_node(state: AgentState):
    query = state["query"]

    res = requests.get(
        "http://localhost:8000/search",
        params={"query": query},
        timeout=30
    )

    data = res.json()
    state["context"] = data.get("results", [])

    return state

# 🔹 Node 3 — Answer Node
def answer_node(state: AgentState):
    context = "\n".join(state.get("context", []))
    question = state["query"]

    answer = f"""
Answer based only on transcript:

Context:
{context}

Question: {question}
"""
    state["answer"] = answer
    return state

# 🔹 Graph Build
graph = StateGraph(AgentState)

graph.add_node("planner", planner)
graph.add_node("tool", tool_node)
graph.add_node("answer", answer_node)

graph.set_entry_point("planner")

graph.add_edge("planner", "tool")
graph.add_edge("tool", "answer")
graph.add_edge("answer", END)

# 🔹 EXPORT THIS
app_graph = graph.compile()