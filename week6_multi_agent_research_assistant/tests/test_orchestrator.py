from agents.orchestrator import build_graph

graph = build_graph()

initial_state = {
    "query": "Artificial Intelligence in Banking"
}

result = graph.invoke(
    initial_state
)

print(result["summary"])