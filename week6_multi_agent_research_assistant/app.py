import time

import streamlit as st

from agents.orchestrator import (
    build_graph,
    run_planner,
    run_search,
    run_summarizer
)

from utils.pdf_generator import create_pdf


st.set_page_config(
    page_title="Multi-Agent Research Assistant",
    page_icon="🔍",
    layout="wide"
)

st.title(
    "🔍 Multi-Agent Research Assistant"
)

st.markdown(
    """
    Enter a research topic and generate a structured research report using
    a Multi-Agent AI workflow powered by OpenAI, Tavily and LangGraph.
    """
)

st.divider()

query = st.text_input(
    "Research Topic",
    placeholder="Example: Future of Small Language Models"
)

execution_mode = st.radio(
    "Execution Mode",
    [
        "LangGraph Orchestration",
        "Direct Agent Execution"
    ],
    horizontal=True
)

submit = st.button(
    "🚀 Generate Report",
    use_container_width=True
)

if submit:

    if not query:

        st.warning(
            "Please enter a research topic."
        )

    else:

        total_start = time.time()

        # -----------------------------------
        # LangGraph Mode
        # -----------------------------------

        if execution_mode == "LangGraph Orchestration":

            status = st.status(
                "Running LangGraph Workflow...",
                expanded=True
            )

            graph = build_graph()

            result = graph.invoke(
                {
                    "query": query
                }
            )

            total_time = round(
                time.time() - total_start,
                2
            )

            status.write(
                "✓ Planner Node Executed"
            )

            status.write(
                "✓ Search Node Executed"
            )

            status.write(
                "✓ Summarizer Node Executed"
            )

            status.write(
                f"🏁 Total Execution Time: {total_time:.2f} sec"
            )

            status.update(
                label="✅ LangGraph Workflow Complete",
                state="complete"
            )

        # -----------------------------------
        # Direct Agent Mode
        # -----------------------------------

        else:

            status = st.status(
                "Running Direct Agent Execution...",
                expanded=True
            )

            state = {
                "query": query
            }

            status.write(
                "🧠 Planner Agent Started..."
            )

            state, planner_time = run_planner(
                state
            )

            status.write(
                f"✅ Planner Agent Completed ({planner_time:.2f} sec)"
            )

            status.write(
                "🔎 Search Agent Started..."
            )

            state, search_time = run_search(
                state
            )

            status.write(
                f"✅ Search Agent Completed ({search_time:.2f} sec)"
            )

            status.write(
                "📝 Summarizer Agent Started..."
            )

            state, summarizer_time = run_summarizer(
                state
            )

            status.write(
                f"✅ Summarizer Agent Completed ({summarizer_time:.2f} sec)"
            )

            total_time = round(
                time.time() - total_start,
                2
            )

            status.write(
                "----------------------------------"
            )

            status.write(
                f"🏁 Total Execution Time: {total_time:.2f} sec"
            )

            status.update(
                label="✅ Direct Agent Execution Complete",
                state="complete",
                expanded=True
            )

            result = state

        # -----------------------------------
        # Report
        # -----------------------------------

        st.divider()

        st.header(
            "📄 Research Report"
        )

        st.markdown(
            result["summary"]
        )

        # -----------------------------------
        # Sources
        # -----------------------------------

        st.divider()

        st.subheader(
            "🔗 Sources"
        )

        if "sources" in result:

            for source in result["sources"]:

                st.markdown(
                    f"- [{source['title']}]({source['url']})"
                )

        # -----------------------------------
        # PDF Download
        # -----------------------------------

        pdf_data = create_pdf(
            result["summary"],
            result.get(
                "sources",
                []
            )
        )

        st.download_button(
            label="📥 Download Report as PDF",
            data=pdf_data,
            file_name="research_report.pdf",
            mime="application/pdf",
            use_container_width=True
        )

st.divider()

st.markdown(
    """
    ### Developer

    Developed by **Devesh Gupta**
    - 🌐 Live App: https://devesh-research-assistant.streamlit.app/
    - 🌐 GitHub: https://github.com/deveshusg
    - 💼 LinkedIn: https://www.linkedin.com/in/gupta-devesh/

    ---
    Built using:

    - OpenAI
    - Tavily
    - LangGraph
    - Streamlit
    """
)