# 🔍 Multi-Agent Research Assistant

Capstone Project for Week 6 of the Gen-AI Assignments series.

A Multi-Agent AI Research Assistant built using OpenAI, Tavily, LangGraph, LangChain, and Streamlit.

The application accepts a research topic, performs web-based research using specialized AI agents, and generates a structured research report with references and downloadable PDF output.

---

# Project Overview

Traditional chatbots rely primarily on pre-trained knowledge and may not provide up-to-date information.

This project demonstrates how multiple specialized AI agents can collaborate to:

* Understand a research topic
* Create a research plan
* Gather current information from the web
* Generate a structured research report
* Provide source references
* Export reports as PDF documents

---

# Features

## 🧠 Multi-Agent Architecture

The system consists of three specialized AI agents.

### Planner Agent

Responsibilities:

* Understands the research topic
* Breaks the topic into research tasks
* Creates a structured research plan

### Search Agent

Responsibilities:

* Searches the web using Tavily
* Collects relevant information
* Stores references and source links

### Summarizer Agent

Responsibilities:

* Synthesizes gathered information
* Generates a structured report
* Produces final insights and recommendations

---

## ⚙️ Dual Execution Modes

### 1. LangGraph Orchestration

Uses LangGraph to orchestrate workflow execution through a graph-based architecture.

```text
START
  │
  ▼
Planner
  │
  ▼
Search
  │
  ▼
Summarizer
  │
  ▼
END
```

### 2. Direct Agent Execution

Executes agents sequentially while displaying:

* Planner execution time
* Search execution time
* Summarizer execution time
* Total workflow execution time

This mode provides enhanced observability and debugging.

---

## 📄 Research Report Generation

The generated report includes:

* Executive Summary
* Key Findings
* Industry Trends
* Risks and Challenges
* Future Outlook
* References

---

## 🔗 Source Attribution

All retrieved sources are displayed as clickable links.

Users can:

* Verify information
* Explore original source material
* Improve transparency and trust

---

## 📥 PDF Export

Generated reports can be downloaded as PDF documents.

The exported PDF includes:

* Complete research report
* References section
* Source URLs

---

# System Architecture

```text
User Query
     │
     ▼
Streamlit UI
     │
     ▼
Execution Mode
     │
 ┌───┴────────────┐
 │                │
 ▼                ▼
LangGraph     Direct Agent
Workflow      Execution
 │                │
 └──────┬─────────┘
        │
        ▼
 Planner Agent
        │
        ▼
 Search Agent
        │
        ▼
 Summarizer Agent
        │
        ▼
 Research Report
```
---

# Technology Stack

| Component              | Technology                 |
| ---------------------- | -------------------------- |
| LLM                    | OpenAI GPT-4o Mini         |
| Agent Framework        | LangGraph                  |
| Agent Utilities        | LangChain                  |
| Web Search             | Tavily                     |
| Frontend               | Streamlit                  |
| PDF Generation         | ReportLab                  |
| Environment Management | Python Virtual Environment |

---

# Project Structure

```text
Week 6 - Capstone Project - Multi Agent Research Assistant
│
├── agents
│   ├── __init__.py
│   ├── orchestrator.py
│   ├── planner.py
│   ├── search.py
│   ├── state.py
│   └── summarizer.py
│
├── data
│   ├── research_report_1.txt
│   ├── research_report_2.txt
│   └── research_report.pdf
│
├── diagrams
│   └── architecture.png
│
├── docs
│   ├── ARCHITECTURE.md
│   ├── FOUNDATIONS.md
│   └── PROJECT_CHECKLIST.md
│
├── notebooks
│   ├── test_langgraph.py
│   ├── test_llm.py
│   └── test_tavily.py
│
├── prompts
│   ├── planner_prompt.txt
│   ├── search_prompt.txt
│   └── summarizer_prompt.txt
│
├── tests
│   ├── test_orchestrator.py
│   ├── test_pipeline.py
│   ├── test_planner.py
│   ├── test_search.py
│   └── test_summarizer.py
│
├── utils
│   ├── __init__.py
│   ├── llm.py
│   ├── pdf_generator.py
│   ├── prompt_loader.py
│   └── web_search.py
│
├── .env.example
├── .gitignore
├── app.py
├── README.md
└── requirements.txt
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/deveshusg/Gen-AI-Assignments.git

cd "Gen-AI-Assignments/Week 6 - Capstone Project - Multi Agent Research Assistant"
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Mac/Linux

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key

TAVILY_API_KEY=your_tavily_api_key
```

---

# Running The Application

```bash
streamlit run app.py
```

Application launches locally at:

```text
http://localhost:8501
```

---

# Example Query

```text
Future of Small Language Models
```

---

# Example Workflow

```text
User Query
      ↓
Planner Agent
      ↓
Search Agent
      ↓
Summarizer Agent
      ↓
Research Report
```

---

# Learning Outcomes

This project demonstrates practical understanding of:

* Multi-Agent Systems
* Agent Orchestration
* LangGraph
* LangChain
* State Management
* Prompt Engineering
* Tool Calling
* Web Search Integration
* Streamlit Development
* LLM Application Design

---

# Future Enhancements

Potential future improvements include:

* Memory-enabled agents
* Retrieval-Augmented Generation (RAG)
* Vector databases
* PDF upload and analysis
* Citation verification
* Fact-checking agent
* Research history persistence
* Multi-user support
* Cloud deployment

---

# Developer

**Devesh Gupta**

GitHub: https://github.com/deveshusg

LinkedIn: https://www.linkedin.com/in/gupta-devesh/

---

# License

This project is intended for educational, learning, and portfolio purposes.
