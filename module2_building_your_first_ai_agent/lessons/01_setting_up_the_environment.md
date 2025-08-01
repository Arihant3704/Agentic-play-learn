# Lesson 1: Setting up Your Development Environment

## Introduction

Welcome to Module 2! In this module, we will move from theory to practice and start building our own AI agents. The first step is to set up a proper development environment. This will ensure that you have all the necessary tools and libraries to follow along with the examples and build your own projects.

## Prerequisites

Before we begin, make sure you have the following installed on your system:

*   **Python:** This course uses Python. If you don't have it installed, you can download it from the official [Python website](https://www.python.org/downloads/). We recommend using Python 3.8 or higher.
*   **A code editor:** We recommend using a modern code editor like [Visual Studio Code](https://code.visualstudio.com/), which has excellent support for Python development.

## Step 1: Create a Virtual Environment

A virtual environment is a self-contained directory that has its own Python installation and a set of installed packages. Using a virtual environment is highly recommended as it prevents conflicts between the dependencies of different projects.

To create a virtual environment, open your terminal or command prompt and run the following command:

```bash
python -m venv my-agent-env
```

This will create a new directory called `my-agent-env` which contains the virtual environment. To activate the virtual environment, use the following command:

*   **On macOS and Linux:**

    ```bash
    source my-agent-env/bin/activate
    ```

*   **On Windows:**

    ```bash
    .\my-agent-env\Scripts\activate
    ```

Once the virtual environment is activated, you will see its name in your terminal prompt.

## Step 2: Install Necessary Libraries

Now that we have our virtual environment set up, we can install the libraries we'll be using to build our agents. For this course, we will primarily be using the **LangChain** framework and the **OpenAI** API.

To install these libraries, run the following command in your activated virtual environment:

```bash
pip install langchain openai
```

This will download and install the latest versions of LangChain and the OpenAI Python library.

## Step 3: Get an OpenAI API Key

To use the OpenAI API, you will need an API key. If you don't already have one, you can sign up for an account on the [OpenAI website](https://platform.openai.com/) and create a new API key.

Once you have your API key, it's important to keep it secure. We recommend storing it as an environment variable rather than hardcoding it into your scripts.

To set an environment variable, you can use the following command:

*   **On macOS and Linux:**

    ```bash
    export OPENAI_API_KEY='your-api-key-here'
    ```

*   **On Windows:**

    ```bash
    setx OPENAI_API_KEY "your-api-key-here"
    ```

Replace `your-api-key-here` with your actual OpenAI API key. You will need to restart your terminal for this change to take effect.

## Conclusion

Your development environment is now ready! You have a virtual environment with the necessary libraries installed and your OpenAI API key is securely stored. In the next lesson, we will introduce the LangChain framework and start building our first simple AI agent.
