from agent.langgraph_agent import app_graph


def main():
    print("🚀 MCP + LangGraph RAG Chatbot Ready")
    print("Type 'exit' to quit\n")

    while True:
        query = input("Ask question about video: ")

        # Exit condition
        if query.strip().lower() in ["exit", "quit"]:
            print("👋 Exiting...")
            break

        try:
            # 🔹 Pass query into LangGraph state
            result = app_graph.invoke({"query": query})

            # 🔹 Get answer from state
            answer = result.get("answer", "No answer generated.")

            print("\n📌 Final Answer:\n")
            print(answer)
            print("\n" + "-" * 50 + "\n")

        except Exception as e:
            print(f"❌ Error: {str(e)}\n")


if __name__ == "__main__":
    main()