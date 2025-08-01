# Module 3 Assignment: Build a Multi-Agent Research Team

## Introduction

In this assignment, you will apply the advanced concepts you've learned in this module to build a multi-agent system. You will create a team of AI agents that collaborate to research a topic and produce a summary report.

## The Challenge

Your task is to create a multi-agent system that can research a given topic and write a brief report. The system should consist of at least two different types of agents:

1.  **Research Agent:** This agent is responsible for searching the web to find information about the given topic.
2.  **Writer Agent:** This agent takes the information gathered by the research agent and writes a coherent summary.

### Requirements

1.  **Agent Roles:** You must define at least two distinct agent roles (e.g., researcher, writer). You can add more roles if you like (e.g., editor, critic).

2.  **Agent Collaboration:** The agents must collaborate to complete the task. The research agent should pass its findings to the writer agent.

3.  **Tool Integration:** The research agent must use a search tool to find information online. You can use a library like `duckduckgo-search` or an API like SerpAPI.

4.  **Planning and Decomposition:** The system should be able to take a high-level goal (e.g., "Research the benefits of exercise") and break it down into steps for the agents to follow.

5.  **Output:** The final output of the system should be a text report that summarizes the research findings.

### High-Level Architecture

You can use a hierarchical architecture where a "manager" or "orchestrator" function controls the workflow:

1.  The manager receives the research topic.
2.  The manager instructs the research agent to find information.
3.  The research agent returns its findings (e.g., a list of URLs or text snippets).
4.  The manager passes the findings to the writer agent.
5.  The writer agent generates the summary report.
6.  The manager returns the final report.

### Starter Code and Hints

You can use a framework like LangChain or AutoGen to build your multi-agent system. Here are some hints to get you started:

*   **LangChain:** You can create different agent objects for each role and then write a Python script to orchestrate the interaction between them.
*   **AutoGen:** AutoGen is a framework specifically designed for building multi-agent systems. It provides a high-level API for defining agents and their interactions.

Here is a conceptual code snippet to illustrate the idea:

```python
# This is a conceptual example, not runnable code

from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_openai import OpenAI

# 1. Define Tools
search = DuckDuckGoSearchRun()

# 2. Create Researcher Agent
researcher = ... # An agent with the search tool

# 3. Create Writer Agent
writer = ... # An agent that can summarize text

# 4. Orchestrate the workflow
def run_research_team(topic: str):
    # Step 1: Researcher finds information
    research_results = researcher.run(f"Find information about {topic}")
    
    # Step 2: Writer summarizes the results
    report = writer.run(f"Write a summary of the following information: {research_results}")
    
    return report

# Run the team
final_report = run_research_team("the benefits of exercise")
print(final_report)

```

### Submission

To complete the assignment, you should have a Python script that implements the multi-agent research team. The script should be well-commented and should clearly show how the agents are defined and how they collaborate. You should also include a `requirements.txt` file listing the necessary libraries.

This is a challenging but rewarding assignment. Good luck!
