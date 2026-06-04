# 🔍 Multi-Agent Research Assistant

### 🚀 Live Demo

**Streamlit Application:**
https://devesh-research-assistant.streamlit.app/

---

## Project Overview

A Multi-Agent AI Research Assistant built using OpenAI, Tavily, LangGraph, LangChain, and Streamlit.

The application accepts a research topic, performs web-based research using specialized AI agents, and generates a structured research report with references and downloadable PDF output.

The project demonstrates how multiple AI agents can collaborate to solve a complex task by dividing responsibilities across planning, information retrieval, and summarization.

---

## Live Application

👉 https://devesh-research-assistant.streamlit.app/

Try queries such as:

* Future of Small Language Models
* Impact of AI on Credit Risk Modeling
* Future of Agentic AI
* Applications of Generative AI in Banking
* Autonomous AI Agents in Healthcare

---

# Features

## 🧠 Multi-Agent Architecture

The application consists of three specialized AI agents.

### Planner Agent

Responsibilities:

* Understands the research topic
* Breaks the problem into research tasks
* Creates a research plan
* Defines research objectives

### Search Agent

Responsibilities:

* Searches the web using Tavily Search
* Collects current information
* Retrieves relevant sources
* Stores references and URLs

### Summarizer Agent

Responsibilities:

* Synthesizes gathered information
* Generates a structured report
* Produces final insights
* Organizes information into readable sections

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

## 📊 Execution Monitoring

The application displays:

* Planner Agent execution progress
* Search Agent execution progress
* Summarizer Agent execution progress
* Individual execution times
* Total workflow execution time

This allows users to observe how the workflow executes in real time.

---

## 📄 Research Report Generation

Generated reports include:

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
* Explore source material
* Review original references
* Improve trust and transparency

---

## 📥 PDF Export

Generated reports can be downloaded as PDF documents.

The exported PDF contains:

* Full research report
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
        │
        ▼
 PDF Export
```

---

# Technology Stack

| Component              | Technology                 |
| ---------------------- | -------------------------- |
| LLM                    | OpenAI GPT-4o Mini         |
| Agent Framework        | LangGraph                  |
| Agent Utilities        | LangChain                  |
| Web Search             | Tavily Search              |
| Frontend               | Streamlit                  |
| PDF Generation         | ReportLab                  |
| Environment Management | Python Virtual Environment |

---

# Project Structure

```text
week6_multi_agent_research_assistant
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
│   └── .gitkeep
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
├── requirements.txt
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/deveshusg/Gen-AI-Assignments.git

cd week6_multi_agent_research_assistant
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

Create a `.env` file in the project root.

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
      ↓
PDF Export
```

---

# Example Research Topics

### Artificial Intelligence

* Future of Small Language Models
* Agentic AI Applications
* Autonomous AI Systems
* AI in Financial Services

### Banking & Risk

* AI in Credit Risk Modeling
* Future of Basel Regulations
* Generative AI in Banking
* Explainable AI in Risk Management

### Technology

* Future of Quantum Computing
* Edge AI Applications
* Cybersecurity Trends
* Future of Robotics

---

# Learning Outcomes

This project demonstrates practical understanding of:

* Multi-Agent Systems
* Agent Orchestration
* LangGraph
* LangChain
* State Management
* Prompt Engineering
* Tool Integration
* Web Search Integration
* LLM Application Development
* Streamlit Development
* PDF Report Generation
* Workflow Monitoring

---

# Challenges Solved

During development the following challenges were addressed:

* Multi-agent workflow design
* LangGraph orchestration
* State management across agents
* Real-time execution monitoring
* Web search integration
* PDF generation
* Environment variable management
* Streamlit Cloud deployment
* File path handling across environments

---

# Future Enhancements

Potential future improvements include:

* Memory-enabled agents
* Retrieval-Augmented Generation (RAG)
* Vector database integration
* PDF upload and analysis
* Fact-checking agent
* Citation verification
* Report history persistence
* Multi-user support
* Authentication
* Cloud database integration
* Agent collaboration workflows

---

# Developer

**Devesh Gupta**

🌐 Live Application
https://devesh-research-assistant.streamlit.app/

💻 GitHub
https://github.com/deveshusg

🔗 LinkedIn
https://www.linkedin.com/in/gupta-devesh/

---

# License

This project is intended for educational, learning, and portfolio purposes.

---

## Acknowledgements

This project was built using:

* OpenAI
* Tavily
* LangChain
* LangGraph
* Streamlit
* ReportLab

and was developed as the Week 6 Capstone Project in the Gen AI Assignments series.
