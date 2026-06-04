# Multi-Agent Research Assistant

# Architecture Document

---

# 1. Project Overview

## Objective

Build a Multi-Agent Research Assistant that accepts a research question from a user, performs web research using specialized AI agents, and generates a structured research report.

The project demonstrates:

* Multi-Agent Systems
* Agent Orchestration
* Tool Calling
* LangGraph Workflows
* State Management
* Web Search Integration
* Streamlit Deployment

---

# 2. Business Problem

Traditional chatbots often generate answers solely from their training data and may not have access to current information.

A research assistant should be able to:

1. Understand the research topic.
2. Break the topic into smaller research tasks.
3. Gather current information from the internet.
4. Synthesize findings.
5. Present a structured report.

This project addresses that requirement using multiple specialized agents.

---

# 3. User Story

As a user,

I want to submit a research topic,

So that I receive a comprehensive research report generated from current web information.

### Example Input

```text
Research the impact of Artificial Intelligence on Banking
```

### Example Output

```text
Executive Summary

Key Findings

Applications

Risks

Future Trends

Sources
```

---

# 4. System Architecture

The application follows a sequential multi-agent architecture.

```text
User Query
     │
     ▼
Orchestrator Agent
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
Final Research Report
```

---

# 5. Architecture Pattern

## Pattern Used

Sequential Orchestration Pattern

### Why This Pattern?

Advantages:

* Easy to understand
* Easy to debug
* Easy to explain in interviews
* Natural fit for research workflows
* Compatible with LangGraph

### Alternative Patterns Not Used

#### Parallel Pattern

```text
Planner
   │
 ┌─┴─┐
 ▼   ▼
A     B
 └─┬─┘
   ▼
Summary
```

Reason not used:

* Additional complexity
* Not required for MVP

#### Hierarchical Pattern

```text
Manager Agent
      │
 ┌────┼────┐
 ▼    ▼    ▼
A     B    C
```

Reason not used:

* More complex coordination
* Unnecessary for assignment scope

---

# 6. Agent Definitions

## 6.1 Orchestrator Agent

### Purpose

Controls workflow execution.

### Responsibilities

* Receive user request
* Manage graph execution
* Route data between agents
* Maintain state
* Return final result

### Input

```text
User Query
```

### Output

```text
Final Research Report
```

---

## 6.2 Planner Agent

### Purpose

Convert user query into research tasks.

### Responsibilities

* Analyze topic
* Identify research dimensions
* Generate research plan
* Create task list

### Example

Input:

```text
Research AI in Banking
```

Output:

```text
1. Market Overview
2. Banking Applications
3. Benefits
4. Risks
5. Future Trends
```

---

## 6.3 Search Agent

### Purpose

Collect information from the web.

### Responsibilities

* Execute web searches
* Gather evidence
* Retrieve sources
* Store findings

### Tool Used

Tavily Search API

### Output

```text
Search Results
URLs
Source Content
```

---

## 6.4 Summarizer Agent

### Purpose

Transform findings into a structured report.

### Responsibilities

* Consolidate information
* Remove redundancy
* Generate final report
* Format output

### Output Sections

```text
Executive Summary

Key Findings

Risks

Future Trends

References
```

---

# 7. State Design

## Purpose

LangGraph uses state to pass information between nodes.

The state acts as shared memory.

---

## ResearchState

```python
from typing import TypedDict

class ResearchState(TypedDict):
    query: str
    plan: str
    search_results: str
    summary: str
```

---

## State Evolution

### Initial State

```python
{
    "query": "Research AI in Banking"
}
```

### After Planner

```python
{
    "query": "Research AI in Banking",
    "plan": "..."
}
```

### After Search

```python
{
    "query": "Research AI in Banking",
    "plan": "...",
    "search_results": "..."
}
```

### After Summarizer

```python
{
    "query": "Research AI in Banking",
    "plan": "...",
    "search_results": "...",
    "summary": "..."
}
```

---

# 8. LangGraph Workflow Design

## Workflow

```text
START
  │
  ▼
Planner Node
  │
  ▼
Search Node
  │
  ▼
Summarizer Node
  │
  ▼
END
```

---

## Node Mapping

| Node            | Agent            |
| --------------- | ---------------- |
| Planner Node    | Planner Agent    |
| Search Node     | Search Agent     |
| Summarizer Node | Summarizer Agent |

---

# 9. Prompt Design

## Planner Prompt

### Goal

Generate research tasks.

Example:

```text
Break the topic into research tasks.
Return a numbered list.
```

---

## Search Prompt

### Goal

Extract relevant information.

Example:

```text
Analyze search results and identify key facts.
```

---

## Summarizer Prompt

### Goal

Create final report.

Example:

```text
Generate a structured research report using the provided findings.
```

---

# 10. Tool Architecture

## Tavily Search Tool

Purpose:

* Internet search
* Source retrieval
* Content extraction

Workflow:

```text
User Query
     │
     ▼
Search Agent
     │
     ▼
Tavily API
     │
     ▼
Search Results
```

---

# 11. Frontend Architecture

## Framework

Streamlit

---

## Components

### Input Box

Accept research question.

### Submit Button

Start workflow execution.

### Output Area

Display report.

---

## UI Flow

```text
User Input
      │
      ▼
Submit
      │
      ▼
LangGraph Workflow
      │
      ▼
Report Display
```

---

# 12. Project Structure

```text
Multi-Agent Research Assistant
│
├── agents
│   ├── orchestrator.py
│   ├── planner.py
│   ├── search.py
│   └── summarizer.py
│
├── prompts
│   ├── planner_prompt.txt
│   ├── search_prompt.txt
│   └── summarizer_prompt.txt
│
├── utils
│   ├── llm.py
│   └── web_search.py
│
├── docs
│   ├── FOUNDATIONS.md
│   ├── ARCHITECTURE.md
│   └── PROJECT_CHECKLIST.md
│
├── tests
│
├── app.py
│
├── requirements.txt
│
└── README.md
```

---

# 13. Error Handling Strategy

## Search Failure

Action:

* Retry search
* Return graceful error message

---

## API Failure

Action:

* Log error
* Notify user

---

## Empty Results

Action:

* Request broader search query

---

# 14. Scalability Roadmap

Future agents may include:

## Fact Checker Agent

Validate findings.

## Citation Agent

Generate references.

## PDF Reader Agent

Analyze uploaded files.

## Database Agent

Query structured data.

## Visualization Agent

Generate charts.

The architecture should support these additions without major redesign.

---

# 15. MVP Scope

The initial version will include only:

* Query Input
* Planner Agent
* Search Agent
* Summarizer Agent
* LangGraph Workflow
* Streamlit Interface
* Tavily Search Integration

---

# Out Of Scope

The following features are intentionally excluded:

* RAG
* Vector Databases
* Memory Systems
* User Authentication
* Multi-User Support
* File Uploads
* Chat History
* Advanced Agent Collaboration

---

# Success Criteria

The project is considered successful if:

1. User enters a research topic.
2. Planner generates research tasks.
3. Search agent retrieves web information.
4. Summarizer generates a report.
5. Streamlit displays results.
6. Workflow executes through LangGraph.
7. Application is deployed successfully.

---

# Key Learning Outcomes

After completing this project, the developer should understand:

* AI Agents
* Multi-Agent Systems
* Agent Orchestration
* LangGraph
* State Management
* Tool Calling
* Prompt Engineering
* Web Search Integration
* Streamlit Deployment
* Production AI Workflows

```
```
