# Lesson 4: Interacting with Your AI Agent

## Introduction

Now that you have the code for your simple AI agent, it's time to bring it to life! In this lesson, we will walk through how to run the agent, interact with it, and understand its responses. This is where you get to see the magic of agentic AI in action.

## Running the Agent

To run your agent, follow these steps:

1.  **Save the code:** Make sure you have saved the code from the previous lesson as a Python file (e.g., `simple_agent.py`).
2.  **Open your terminal:** Open a terminal or command prompt.
3.  **Activate your virtual environment:** If you created a virtual environment, make sure to activate it.
4.  **Run the script:** Execute the Python script from your terminal:

    ```bash
    python simple_agent.py
    ```

If everything is set up correctly, you should see the message: `Simple AI Agent Initialized. Ask me a question.`

## Interacting with the Agent

Now you can start asking your agent questions. Let's try a few examples:

### Example 1: A Simple Math Question

**You:** `What is 5 + 5?`

When you ask this question, you will see a detailed output from the agent because we set `verbose=True`. It will look something like this:

```
> Entering new AgentExecutor chain...
I need to calculate 5 + 5.
Action: Calculator
Action Input: 5 + 5
Observation: 10
Thought: I now know the final answer.
Final Answer: 10

> Finished chain.
Agent: 10
```

Let's break down this output:

*   **`Entering new AgentExecutor chain...`**: This indicates that the agent is starting a new task.
*   **`I need to calculate 5 + 5.`**: This is the agent's internal thought. It has correctly identified that it needs to perform a calculation.
*   **`Action: Calculator`**: The agent has decided to use the `Calculator` tool.
*   **`Action Input: 5 + 5`**: This is the input that the agent is providing to the `Calculator` tool.
*   **`Observation: 10`**: This is the output from the `Calculator` tool.
*   **`Thought: I now know the final answer.`**: The agent has received the result from the tool and is now ready to give the final answer.
*   **`Final Answer: 10`**: This is the agent's final answer to your question.

### Example 2: Asking for the Date

**You:** `What is the date today?`

Again, you will see the agent's thought process:

```
> Entering new AgentExecutor chain...
I need to find out the current date.
Action: Current Date
Action Input: 
Observation: 2025-07-26
Thought: I now know the final answer.
Final Answer: Today's date is 2025-07-26.

> Finished chain.
Agent: Today's date is 2025-07-26.
```

In this case, the agent correctly identified that it needed to use the `Current Date` tool.

## Experiment and Explore

The best way to learn is by experimenting. Try asking your agent different questions and see how it responds. Here are a few ideas:

*   Ask it more complex math problems.
*   Ask it a question that requires both tools (e.g., "What is the date tomorrow?"). Note: The current agent is not smart enough to answer this, which is a good learning opportunity!
*   Try to trick the agent. What happens if you ask it a question it can't answer?

## Conclusion

By interacting with your agent, you can gain a deeper understanding of how it works. The `verbose` output is a powerful tool for debugging and for seeing the world from the agent's perspective. In the next lesson, we will give you an assignment to modify and improve this agent.