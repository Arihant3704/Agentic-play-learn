# Lesson 4: Deep Dive Case Study - The AI Co-Pilot Agent

## Introduction
This lesson provides a detailed technical blueprint for the "AI Co-Pilot" agent, named Axel. We will structure this as a plan for the Gemma 3n Impact Challenge, focusing on how the agent uses tools and reasoning to provide proactive assistance.

## 1. The Agentic Loop: Continuous Monitoring and Advising

Axel doesn't wait for commands. It runs in a continuous background loop:
1.  **Perceive:** Every few minutes, the agent gathers data from its tools: vehicle status, current route and traffic, and weather forecast.
2.  **Reason:** It sends this combined data to Gemma 3n with a specific prompt to check if any conditions warrant a driver notification.
3.  **Act:** If Gemma's reasoning determines a notification is needed, the agent uses its voice tool to speak to the driver.

## 2. System Architecture & Tools

### Tool 1: `VehicleAPI` (Interface with the Car)

This tool would be a software layer that communicates with the car's CAN bus or a simulated vehicle environment.

**Functionality:**
-   `get_vehicle_state()`: Returns a JSON object with key metrics.
    -   `{"speed": 65, "battery_percent": 45, "tire_pressure_psi": [32, 33, 32, 31], "range_miles": 120}`

### Tool 2: `NavigationAPI` (Maps & Traffic)

This tool would interface with a service like Google Maps or Mapbox.

**Functionality:**
-   `get_route_info()`: Returns data about the current trip.
    -   `{"eta_minutes": 90, "traffic_condition": "heavy", "upcoming_terrain": "hilly"}`
-   `find_poi_on_route(type="charging_station")`: Finds points of interest.

### Tool 3: `WeatherAPI`

Interfaces with a weather service like OpenWeatherMap.

**Functionality:**
-   `get_weather_on_route()`: Returns weather conditions ahead.
    -   `{"condition": "rain", "intensity": "heavy", "temperature_f": 45}`

### The Reasoning Core (Gemma 3n)

Gemma's role is to be the proactive decision-maker. It connects the dots between the different data sources.

**The "Should I Intervene?" Prompt Template:**

```text
You are Axel, an AI Co-Pilot. Your job is to ensure the driver is safe and efficient. You will be given the current state of the vehicle, the route, and the weather. Analyze this data to determine if you should provide a proactive suggestion. If no suggestion is needed, respond with "None". Otherwise, formulate a clear, concise, and helpful suggestion for the driver.

**Vehicle State:**
{{vehicle_state}}

**Route Information:**
{{route_info}}

**Weather Forecast:**
{{weather_info}}

Analyze the combined data. Is there a potential safety issue, a significant efficiency gain, or a major convenience improvement available? If so, what is your suggestion?

Suggestion:
```

## 3. The Main Agentic Loop

The application logic continuously runs this cycle.

```python
# Conceptual Code for the AI Co-Pilot's main loop

# while driver_is_on_trip():
#     # 1. Perceive
#     vehicle_data = vehicle_api.get_vehicle_state()
#     route_data = navigation_api.get_route_info()
#     weather_data = weather_api.get_weather_on_route()
#
#     # 2. Reason
#     suggestion = gemma_agent.run(
#         vehicle_state=vehicle_data, 
#         route_info=route_data, 
#         weather_info=weather_data
#     )
#
#     # 3. Act
#     if suggestion != "None":
#         speech_tool.speak(suggestion)
#         log_suggestion(suggestion)
#
#     time.sleep(120) # Wait for 2 minutes before the next check
```

This architecture creates a truly agentic system that provides value proactively, making it a strong candidate for an impact-focused hackathon.