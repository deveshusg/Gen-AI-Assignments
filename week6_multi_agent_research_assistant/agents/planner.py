from utils.llm import get_llm
from utils.prompt_loader import load_prompt


def planner_agent(state):

    llm = get_llm()

    planner_prompt = load_prompt(
        "planner_prompt.txt"
    )

    response = llm.invoke(
        f"""
        {planner_prompt}

        User Query:
        {state['query']}
        """
    )

    state["plan"] = response.content

    return state