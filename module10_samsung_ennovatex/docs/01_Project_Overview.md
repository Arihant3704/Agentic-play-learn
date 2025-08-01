# 1. Project Overview: Echo

## 1.1. The Vision
Echo is an on-device, proactive AI companion designed to function as a user's second brain. It operates on the principle of **proactive subtlety**, observing the user's environment and experiences to provide timely, context-aware assistance without explicit commands. By running entirely on-device, Echo guarantees user privacy, low latency, and offline functionality, addressing the core limitations of cloud-based assistants.

## 1.2. Problem Statement Addressed
This project directly tackles **Problem Statement #2: Building the Untethered, Always-On AI Companion** from the Samsung EnnovateX 2025 AI Challenge.

## 1.3. Core Features
- **Advanced Perception (VLM-like):** Echo leverages a sophisticated `PerceptionAgent` that processes raw sensory data (vision, audio) into rich, VLM-like scene descriptions and identified objects, providing a deeper understanding of the environment.
- **Multi-Agent Architecture:** The system is composed of specialized, collaborating internal agents (`PerceptionAgent`, `DecisionAgent`, `ActionAgent`) orchestrated by the main `EchoAgent` for modularity and robustness.
- **Proactive, Agentic Reasoning:** It uses an on-device LLM (`DecisionAgent`) to connect past memories with the present context to anticipate user needs and even issue direct control commands to devices.
- **Privacy by Design:** All data, from sensor input to memory logs and AI models, remains on the user's device. No cloud connection is required for its core functionality.
- **Subtle Human-AI Interaction:** Echo avoids being intrusive by using a graduated system of notifications, from silent lock-screen widgets to haptic feedback and, only when necessary, voice.