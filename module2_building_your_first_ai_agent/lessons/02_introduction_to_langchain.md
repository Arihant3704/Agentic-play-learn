# Lesson 2: Introduction to LangChain

## What is LangChain?

LangChain is a powerful open-source framework that simplifies the development of applications powered by Large Language Models (LLMs). It provides a set of tools and abstractions that make it easy to build complex applications like AI agents, chatbots, and question-answering systems.

At its core, LangChain is all about **composability**. It allows you to chain together different components, such as LLMs, APIs, and data sources, to create sophisticated applications.

## Key Concepts in LangChain

To understand how LangChain works, let's look at some of its key concepts:

### 1. Models

Models are the heart of any LangChain application. LangChain provides a consistent interface for interacting with various LLMs, including those from OpenAI, Hugging Face, and other providers. This makes it easy to switch between different models without having to rewrite your code.

### 2. Prompts

Prompts are the instructions that you give to an LLM. LangChain provides tools for creating and managing prompts, including prompt templates that allow you to create reusable prompts with dynamic inputs.

### 3. Chains

Chains are the core concept of LangChain. A chain is a sequence of calls to models, APIs, or other chains. By chaining together different components, you can build complex workflows and applications.

### 4. Indexes

Indexes are used to structure and retrieve data. LangChain provides tools for working with various data sources, such as text files, PDFs, and databases. This allows you to create applications that can answer questions about your own data.

### 5. Agents

In LangChain, an agent is a special type of chain that can make decisions about which tools to use to achieve a goal. This is what allows us to build agentic AI that can interact with its environment and perform actions.

## Building a Simple Agent with LangChain

Let's take a look at a simple example of how to build an agent with LangChain. This agent will be able to answer questions by searching the web.

First, we need to import the necessary libraries and initialize our LLM and tools:

```python
from langchain.agents import initialize_agent, load_tools
from langchain.llms import OpenAI

# Initialize the LLM
llm = OpenAI(temperature=0)

# Load the tools
tools = load_tools(["serpapi", "llm-math"], llm=llm)
```

Next, we can create our agent by calling the `initialize_agent` function:

```python
# Initialize the agent
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
```

Now we can run our agent with a prompt:

```python
# Run the agent
agent.run("Who is the current president of the United States?")
```

The agent will then use the `serpapi` tool to search the web and find the answer to the question.

## Conclusion

This is just a brief introduction to LangChain. In the following lessons, we will dive deeper into the concepts and tools that LangChain provides, and we will build more complex and powerful AI agents. In the next lesson, we will create our first AI agent from scratch.
