from utils.web_search import search_web


def search_agent(state):

    results = search_web(
        state["query"]
    )

    formatted_results = []
    sources = []

    for result in results["results"]:

        title = result.get("title", "")
        url = result.get("url", "")
        content = result.get("content", "")

        formatted_results.append(
            f"""
Title: {title}

Content:
{content}
"""
        )

        sources.append(
            {
                "title": title,
                "url": url
            }
        )

    state["search_results"] = "\n\n".join(
        formatted_results
    )

    state["sources"] = sources

    return state