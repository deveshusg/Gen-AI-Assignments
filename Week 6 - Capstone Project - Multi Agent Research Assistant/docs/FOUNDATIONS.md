# Multi-Agent Research Assistant
# Phase 0 Foundations

---

# 1. What Is An AI Agent?

## Definition

An AI Agent is a software system that uses a Large Language Model (LLM) to reason about a task, make decisions, use tools, and perform actions toward a goal.

Traditional software follows fixed instructions.

```text
Input
  ↓
Code
  ↓
Output
```

Agents introduce reasoning.

```text
Goal
  ↓
Reason
  ↓
Choose Action
  ↓
Execute
  ↓
Observe Result
  ↓
Repeat
```

This cycle is called the Agent Loop.

---

## Agent Components

### Brain

Usually an LLM.

Examples:

- GPT-4o
- Gemini 2.5
- Claude
- Llama

Responsibilities:

- Understand requests
- Reason
- Plan
- Generate outputs

---

### Memory

Stores information.

Types:

| Type | Purpose |
|--------|--------|
| Short-Term | Current conversation |
| Long-Term | Historical knowledge |
| Working Memory | Current task state |

---

### Tools

Allow agents to interact with external systems.

Examples:

```text
Web Search
Calculator
Database
File Reader
Weather API
Email API
```

Without tools, an agent is just a chatbot.

---

### Actions

Work performed using tools.

Examples:

```text
Search Web
Read PDF
Send Email
Generate Report
```

---

# 2. LLM vs AI Agent

## LLM

```text
Question
  ↓
Answer
```

## Agent

```text
Question
  ↓
Plan
  ↓
Use Tool
  ↓
Analyze
  ↓
Generate Answer
```

### Example

Question:

```text
What is the latest news about OpenAI?
```

LLM:

```text
Only knows training data.
```

Agent:

```text
Searches web.
Reads sources.
Summarizes findings.
```

---

# 3. Tools

Tools are external capabilities an agent can invoke.

Examples:

| Tool | Purpose |
|--------|--------|
| Tavily | Search Internet |
| SQL | Query Data |
| Python | Computation |
| Email | Communication |

---

## Tool Calling Process

```text
User Query
     ↓
Agent
     ↓
Tool Selection
     ↓
Tool Execution
     ↓
Result
     ↓
Agent Response
```

---

# 4. Planning

Planning is the process of decomposing a task into smaller tasks.

Question:

```text
Research Electric Vehicles
```

Planner creates:

```text
1. Find major manufacturers
2. Find market size
3. Find challenges
4. Find opportunities
```

Planning improves:

- Accuracy
- Explainability
- Scalability

---

# 5. Single-Agent Systems

## Architecture

```text
User
  ↓
Agent
  ↓
Tools
```

### Advantages

- Simple
- Easy debugging
- Low cost

### Disadvantages

- Overloaded responsibilities
- Hard to scale
- Reduced specialization

---

# 6. Multi-Agent Systems

## Architecture

```text
Agent A
Agent B
Agent C
```

Each agent specializes.

### Example

| Agent | Responsibility |
|--------|--------|
| Planner | Task decomposition |
| Search | Information gathering |
| Summarizer | Report generation |

---

## Why Multi-Agent?

Specialization improves:

- Quality
- Maintainability
- Explainability

---

# 7. Orchestrator Pattern

Most important concept in this capstone.

## Definition

An Orchestrator Agent controls workflow execution.

It decides:

```text
Which agent runs?
When?
In what order?
What data is passed?
```

---

## Example

User asks:

```text
Research Small Language Models
```

Orchestrator:

```text
Step 1 → Planner
Step 2 → Search
Step 3 → Summarizer
Step 4 → Return Result
```

---

## Benefits

### Centralized Control

One decision-maker.

### Easier Debugging

Clear workflow.

### Scalable

New agents can be added easily.

---

# 8. Agent Communication Patterns

## Sequential

```text
A → B → C
```

Output of A becomes input of B.

Our project uses this pattern.

---

## Parallel

```text
      A
     / \
    B   C
     \ /
      D
```

Multiple agents execute simultaneously.

---

## Hierarchical

```text
Manager
  ↓
Workers
```

Common in enterprise systems.

---

# 9. What Is LangGraph?

LangGraph is a framework for building agent workflows using graph structures.

Developed by LangChain.

Purpose:

```text
State Management
Control Flow
Multi-Agent Workflows
Agent Orchestration
```

---

# 10. Why LangGraph?

Without LangGraph:

```text
Many if-else statements
Complex orchestration
Difficult maintenance
```

With LangGraph:

```text
Nodes
Edges
State
Execution Engine
```

---

# 11. Core Concepts Of LangGraph

## Node

A node performs work.

Examples:

```text
Planner Node
Search Node
Summarizer Node
```

---

## Edge

Connects nodes.

```text
Planner
   ↓
Search
   ↓
Summarizer
```

---

## State

Shared data.

Example:

```python
{
    "query": "",
    "plan": "",
    "search_results": "",
    "summary": ""
}
```

State flows through nodes.

---

# 12. State Management

Most important LangGraph concept.

State acts as the memory of the workflow.

### Initial State

```python
{
    "query": "Research EV Market"
}
```

### After Planner

```python
{
    "query": "Research EV Market",
    "plan": [...]
}
```

### After Search

```python
{
    "query": "Research EV Market",
    "plan": [...],
    "search_results": [...]
}
```

### After Summarizer

```python
{
    "query": "Research EV Market",
    "plan": [...],
    "search_results": [...],
    "summary": "..."
}
```

---

# 13. Research Assistant Design

## User Goal

Provide a topic.

Example:

```text
Research AI in Banking
```

---

## Expected Output

```text
Executive Summary

Key Findings

Risks

Opportunities

Sources
```

---

# 14. Planner Agent

## Responsibilities

```text
Break query into tasks
Create research plan
Identify subtopics
```

### Input

```text
Research AI in Banking
```

### Output

```text
1. Market Overview
2. Applications
3. Risks
4. Future Trends
```

---

# 15. Search Agent

## Responsibilities

```text
Gather information
Use Tavily Search
Collect evidence
Store sources
```

### Input

```text
Research Tasks
```

### Output

```text
Search Results
URLs
Snippets
```

---

# 16. Summarizer Agent

## Responsibilities

```text
Condense findings
Remove duplicates
Create report
```

### Output

```text
Executive Summary
Detailed Findings
Sources
```

---

# 17. Tavily Search

## Purpose

```text
Internet Search
Content Extraction
Research Workflows
```

### Workflow

```text
Question
   ↓
Tavily
   ↓
Results
   ↓
Agent
```

---

# 18. Streamlit Frontend

## Purpose

Provide user interface.

### Components

```text
Text Input
Submit Button
Results Area
```

---

# 19. Complete System Architecture

```text
User
  │
  ▼
Orchestrator
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
Final Report
```

---

# 20. Failure Handling

Potential failures:

| Failure | Solution |
|----------|----------|
| Search timeout | Retry |
| Empty results | Re-search |
| Bad query | Re-plan |
| API error | Graceful handling |

---

# 21. Scalability

Future Agents:

```text
Fact Checker
Citation Generator
PDF Reader
Database Agent
Visualization Agent
```

The architecture should allow these agents to be added without major code changes.

---

# 22. Capstone Learning Outcomes

After completing this project you should understand:

- Agentic AI
- Multi-Agent Systems
- LangGraph
- Orchestration
- State Management
- Tool Calling
- Prompt Engineering
- Tavily Search
- Streamlit Deployment
- Production Workflow Design

---

# Questions

## Fundamental

1. What is an AI Agent?
2. How is an Agent different from an LLM?
3. What is an Orchestrator?
4. Why use Multi-Agent Systems?
5. What is State in LangGraph?
6. What are Nodes and Edges?
7. Why use Tavily?
8. What are the limitations of Single-Agent systems?
9. How does LangGraph differ from LangChain?
10. How would you scale this architecture?

---

# Summary

The Multi-Agent Research Assistant will use:

- LangGraph for orchestration
- OpenAI or Gemini as the reasoning engine
- Tavily for web search
- Streamlit for the user interface

Workflow:

```text
User Query
     ↓
Orchestrator
     ↓
Planner Agent
     ↓
Search Agent
     ↓
Summarizer Agent
     ↓
Research Report
```

This architecture demonstrates:

- Agentic AI
- Multi-Agent Collaboration
- Tool Calling
- Workflow Orchestration
- State Management
- Production-Ready AI Design