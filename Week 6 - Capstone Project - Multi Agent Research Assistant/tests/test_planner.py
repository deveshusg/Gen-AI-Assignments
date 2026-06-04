from agents.planner import planner_agent

state = {
    "query": "Research Artificial Intelligence in Banking"
}

result = planner_agent(state)

print(result["plan"])