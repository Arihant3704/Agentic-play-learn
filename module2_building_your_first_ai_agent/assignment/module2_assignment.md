# Module 2 Assignment: Enhance the AI Agent

## Introduction

In this assignment, you will take the simple AI agent we built in this module and enhance its capabilities. This will require you to write some Python code and apply the concepts you've learned about tools and agents in LangChain.

## The Challenge

Your task is to add a new tool to the agent: a **weather tool**. This tool will allow the agent to answer questions about the current weather in a given location.

### Requirements

1.  **Create a new tool:** You will need to create a new tool that can fetch the current weather. You can use a free weather API for this, such as the [OpenWeatherMap API](https://openweathermap.org/api). You will need to sign up for a free API key.

2.  **Integrate the tool into the agent:** Add the new weather tool to the list of tools that the agent has access to.

3.  **Test the agent:** Test your enhanced agent by asking it questions about the weather, such as:
    *   "What is the weather in London?"
    *   "Is it sunny in Paris?"

### Starter Code

You can start with the code from the "Creating a Simple AI Agent" lesson. You will need to modify it to add the new tool.

Here is a hint for the weather tool function:

```python
import requests

def get_weather(location: str) -> str:
    """Gets the current weather for a given location."""
    # You will need to use a weather API here
    # For example, you can use the OpenWeatherMap API
    # Make sure to handle API keys securely!
    api_key = "YOUR_WEATHER_API_KEY"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    try:
        response = requests.get(base_url, params={"q": location, "appid": api_key, "units": "metric"})
        data = response.json()
        
        if data["cod"] == 200:
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            return f"The weather in {location} is {weather_description} with a temperature of {temperature}°C."
        else:
            return f"Could not retrieve weather for {location}. Error: {data.get('message', 'Unknown error')}"
    except Exception as e:
        return f"An error occurred: {e}"

```

### Submission

To complete the assignment, you should have a Python script that:

1.  Initializes an AI agent with three tools: a calculator, a date tool, and a weather tool.
2.  Can successfully answer questions about math, the current date, and the weather in a given location.

Good luck, and have fun building your enhanced agent!
