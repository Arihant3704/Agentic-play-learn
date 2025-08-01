# Lesson 3: Creating a Simple AI Agent

## Introduction

In this lesson, we will build our very first AI agent from scratch using Python and the LangChain framework. This agent will be a simple "Hello, World!" of agentic AI, but it will demonstrate the core concepts we've discussed.

## The Goal

Our goal is to create an agent that can do two things:

1.  Perform mathematical calculations.
2.  Look up the current date.

To do this, we will give the agent access to two tools: a Python code interpreter and a date tool.

## The Code

Here is the complete Python code for our simple agent. We will break it down step by step.

```python
import os
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from datetime import datetime

# --- 1. Set up the Environment ---

# Make sure you have your OPENAI_API_KEY set as an environment variable
# You can get a key from https://platform.openai.com/
if "OPENAI_API_KEY" not in os.environ:
    print("Error: OPENAI_API_KEY environment variable not set.")
    exit()

# --- 2. Initialize the LLM ---

# We'll use the OpenAI LLM. The temperature is set to 0 to make the output deterministic.
llm = OpenAI(temperature=0)

# --- 3. Define the Tools ---

# Our agent will have access to two tools: a calculator and a date tool.

# The first tool is a simple calculator that uses a Python lambda function.
# This is a simple example of a custom tool.
calculator = Tool(
    name="Calculator",
    func=lambda expression: eval(expression),
    description="Useful for when you need to answer questions about math."
)

# The second tool gets the current date.
def get_current_date(input=""):
    """Returns the current date."""
    return datetime.now().strftime("%Y-%m-%d")

date_tool = Tool(
    name="Current Date",
    func=get_current_date,
    description="Useful for when you need to know the current date."
)

# Create a list of the tools
tools = [calculator, date_tool]

# --- 4. Initialize the Agent ---

# We will use the "zero-shot-react-description" agent type.
# This agent uses the ReAct framework to decide which tool to use based on the tool's description.
agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True  # Set to True to see the agent's thought process
)

# --- 5. Run the Agent ---

print("Simple AI Agent Initialized. Ask me a question.")

while True:
    try:
        prompt = input("You: ")
        if prompt.lower() in ["exit", "quit"]:
            break
        response = agent.run(prompt)
        print(f"Agent: {response}")
    except Exception as e:
        print(f"Error: {e}")

```

### Code Breakdown

1.  **Environment Setup:** The code first checks if the `OPENAI_API_KEY` environment variable is set. This is a crucial step for security.

2.  **LLM Initialization:** We initialize the `OpenAI` LLM. The `temperature` parameter controls the randomness of the output. A value of 0 makes the output more deterministic and predictable.

3.  **Tool Definition:** We define two tools:
    *   `Calculator`: This tool uses a simple `lambda` function to evaluate a mathematical expression. The `eval()` function is used for simplicity, but be aware that it can be a security risk in production environments if not used carefully.
    *   `Current Date`: This tool is a Python function that returns the current date. Each tool has a `name` and a `description`. The `description` is very important, as the agent uses it to decide which tool to use.

4.  **Agent Initialization:** We use the `initialize_agent` function to create our agent. We pass in the tools, the LLM, and the agent type. The `verbose=True` argument allows us to see the agent's internal monologue as it decides which tool to use.

5.  **Agent Execution:** The code enters a loop where it prompts the user for input, runs the agent with the input, and prints the agent's response.

## How to Run the Code

1.  Save the code as a Python file (e.g., `simple_agent.py`).
2.  Make sure you have your `OPENAI_API_KEY` set as an environment variable.
3.  Run the script from your terminal:

    ```bash
    python simple_agent.py
    ```

## Conclusion

Congratulations! You have now created your first AI agent. In the next lesson, we will explore how to interact with this agent and observe its behavior. We will also discuss how to debug and improve our agent.
