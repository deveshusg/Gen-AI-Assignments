from agents.planner import planner_agent
from agents.search import search_agent
from agents.summarizer import summarizer_agent

state = {
    "query": "Artificial Intelligence in Banking"
}

state = planner_agent(state)

state = search_agent(state)

state = summarizer_agent(state)

print(state["summary"])