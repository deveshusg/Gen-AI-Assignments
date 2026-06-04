from utils.llm import get_llm
from utils.prompt_loader import load_prompt


def summarizer_agent(state):

    llm = get_llm()

    summarizer_prompt = load_prompt(
        "summarizer_prompt.txt"
    )

    response = llm.invoke(
        f"""
        {summarizer_prompt}

        Research Topic:
        {state['query']}

        Search Results:
        {state['search_results']}
        """
    )

    state["summary"] = response.content

    return state