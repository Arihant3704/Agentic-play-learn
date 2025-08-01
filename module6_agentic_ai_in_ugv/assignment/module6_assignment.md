# Module 6 Assignment: UGV Mission Simulation

## Introduction
In this assignment, you will design and simulate a mission for an Unmanned Ground Vehicle (UGV). The goal is to apply the concepts of agentic AI for navigation and mission planning in a simulated environment.

## The Challenge
Your task is to create a simulation where a UGV performs a "search and retrieve" mission. The UGV will start at a specific point, navigate through an environment with obstacles to find a designated object, and then return the object to the starting point.

### Requirements
1.  **Simulation Environment:** Create a simple 2D grid-based simulation environment. You can represent this as a 2D array in Python. The environment should include:
    *   A starting point for the UGV.
    *   Obstacles that the UGV must navigate around.
    *   A target object at a specific location.
2.  **UGV Agent:** Create an AI agent to control the UGV. This agent should have the following capabilities:
    *   **Path Planning:** The agent must be able to find a path from its current location to a target location, avoiding obstacles. You can use an algorithm like A*.
    *   **Task Decomposition:** The agent should be able to break down the high-level mission ("find and retrieve the object") into sub-tasks (e.g., "plan path to object," "move to object," "plan path to start," "move to start").
3.  **Execution:** The simulation should visualize the UGV's movement through the grid and print out the agent's status and decisions at each step.

### Submission
To complete the assignment, you should have a Python script that:
1.  Sets up the simulation environment.
2.  Implements the UGV agent with planning and task decomposition logic.
3.  Runs the simulation, showing the UGV successfully completing its mission.
4.  Include a `requirements.txt` file if you use any external libraries.

Good luck building your autonomous UGV!
