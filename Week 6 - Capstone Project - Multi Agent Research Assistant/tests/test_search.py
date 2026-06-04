from agents.search import search_agent

state = {
    "query": "Artificial Intelligence in Banking"
}

result = search_agent(state)

print(result["search_results"])