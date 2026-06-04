from agents.summarizer import summarizer_agent

state = {
    "query": "Artificial Intelligence in Banking",
    "search_results": "AI is increasingly used..."
}

result = summarizer_agent(state)

print(result["summary"])