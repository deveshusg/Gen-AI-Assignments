from typing import TypedDict


class ResearchState(TypedDict):
    query: str
    plan: str
    search_results: str
    sources: list
    summary: str