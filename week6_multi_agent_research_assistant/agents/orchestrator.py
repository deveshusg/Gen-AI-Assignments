import time

from langgraph.graph import StateGraph
from langgraph.graph import START
from langgraph.graph import END

from agents.state import ResearchState

from agents.planner import planner_agent
from agents.search import search_agent
from agents.summarizer import summarizer_agent


def build_graph():

    graph = StateGraph(ResearchState)

    graph.add_node(
        "planner",
        planner_agent
    )

    graph.add_node(
        "search",
        search_agent
    )

    graph.add_node(
        "summarizer",
        summarizer_agent
    )

    graph.add_edge(
        START,
        "planner"
    )

    graph.add_edge(
        "planner",
        "search"
    )

    graph.add_edge(
        "search",
        "summarizer"
    )

    graph.add_edge(
        "summarizer",
        END
    )

    return graph.compile()


def run_planner(state):

    start_time = time.time()

    state = planner_agent(state)

    elapsed = round(
        time.time() - start_time,
        2
    )

    return state, elapsed


def run_search(state):

    start_time = time.time()

    state = search_agent(state)

    elapsed = round(
        time.time() - start_time,
        2
    )

    return state, elapsed


def run_summarizer(state):

    start_time = time.time()

    state = summarizer_agent(state)

    elapsed = round(
        time.time() - start_time,
        2
    )

    return state, elapsed