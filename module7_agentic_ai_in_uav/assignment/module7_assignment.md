# Module 7 Assignment: UAV Delivery Simulation

## Introduction
In this assignment, you will design a simulation for a UAV-based delivery system. You will use agentic AI to manage the delivery process, from receiving an order to dispatching a UAV and confirming the delivery.

## The Challenge
Your task is to create a simulation of a central depot that manages a fleet of UAVs to deliver packages to various locations. 

### Requirements
1.  **Simulation World:** Create a 2D grid representing a small town or area. This grid should have:
    *   A central depot (the UAVs' home base).
    *   Several possible delivery destinations.
2.  **UAV Agents:** Create a class for your UAV agents. Each UAV should have a status (e.g., `idle`, `in-flight`, `charging`) and a battery level.
3.  **Depot Manager Agent:** This is the core of your system. This agent will be responsible for:
    *   **Order Management:** Receiving new delivery orders (you can simulate this with a simple function).
    *   **UAV Dispatch:** Choosing an appropriate UAV for a delivery (e.g., one that is idle and has enough battery).
    *   **Mission Planning:** Sending the chosen UAV to the destination and back to the depot.
    *   **Fleet Monitoring:** Keeping track of the status and battery level of all UAVs.
4.  **Simulation Logic:** The simulation should run in discrete time steps. In each step:
    *   The Depot Manager checks for new orders.
    *   The Depot Manager updates the status of the UAVs (e.g., moving them towards their destination, depleting their battery).
    *   The simulation should print out the state of the system at each time step.

### Submission
To complete the assignment, you should have a Python script that:
1.  Defines the classes for the UAVs and the Depot Manager agent.
2.  Sets up and runs the delivery simulation.
3.  Clearly shows the decision-making process of the Depot Manager agent.
4.  Include a `requirements.txt` file if you use any external libraries.

This assignment will give you a taste of the complexities of managing autonomous systems. Good luck!
