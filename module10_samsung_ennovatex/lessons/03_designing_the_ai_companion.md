# Lesson 3: Designing the "Always-On AI Companion"

## From Problem to Product
Let's design a solution for **Problem Statement #2**. We will call our agent "Echo," as it reflects the user's world.

## Core Concept: A Proactive, Memory-Driven Assistant
Echo is an on-device agent that runs in the background. It continuously processes sensory input (camera, microphone, location) to build a private, on-device "memory stream." It uses this memory to understand the user's context and provide help without being asked.

### The User Journey (Example Scenario)
- **Perception (Memory Creation):** The user is in a hardware store. They take a picture of a specific screw. Echo, running in the background, sees the image and uses an on-device model to classify it: `{"type": "image", "content": "screw, flat-head, 1-inch"}`. This is added to the memory stream.
- **Contextual Awareness:** An hour later, the user is at home, looking at a piece of furniture with an empty screw hole. They look puzzled.
- **Proactive Action (Implicit Intent):** Echo detects the long pause and the visual context. It searches its recent memory stream and finds the memory of the screw from the hardware store. It infers the user's intent.
- **H-AI:** Echo provides a subtle, non-intrusive notification: "Are you looking for the 1-inch flat-head screw you saw at the hardware store earlier?"

### Technical Architecture
- **Core Logic (On-Device LLM):** A highly efficient LLM (like Gemma 3n) that can perform reasoning over the memory stream.
- **Tools (The Senses):
    1.  `VisionTool`:** Continuously analyzes the camera feed for object recognition and scene understanding.
    2.  `AudioTool`:** Processes audio for keywords or environmental sounds (e.g., a baby crying, an alarm).
    3.  `MemoryStream`:** A local, on-device vector database where the agent stores and retrieves experiences.
- **The Agentic Loop:**
    1.  Sensory tools populate the `MemoryStream`.
    2.  The core agent periodically queries the `MemoryStream` and the current sensory input.
    3.  It uses the LLM to reason: "Given the current context and recent memories, is there a high-probability need I can help with?"
    4.  If the probability is high, it acts (e.g., sends a notification).

This design directly addresses the challenge, focusing on on-device memory, proactive assistance, and a truly untethered experience.