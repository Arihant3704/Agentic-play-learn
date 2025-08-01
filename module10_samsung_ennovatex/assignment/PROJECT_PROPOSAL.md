# Project Proposal: Echo - The Untethered, Always-On AI Companion

## 1. Project Title
Echo: The Untethered, Always-On AI Companion

## 2. Team Members
*   Arihant

## 3. Problem Statement
This project directly addresses **Problem Statement #2: Building the Untethered, Always-On AI Companion**.

Modern smartphones are powerful but fundamentally reactive tools. They wait for explicit commands, placing the cognitive burden on the user to know what to ask and when to ask it. This creates a gap between the device's potential and its ability to act as a true partner in our daily lives. The need for constant cloud connectivity for intelligent features also raises significant privacy concerns, as personal data is continuously sent to external servers.

We aim to solve this by creating "Echo," a proactive AI companion that shifts the paradigm from reactive commands to proactive assistance. Echo is "untethered" because it operates entirely on-device, ensuring that the user's personal context and memories remain completely private.

## 4. Our Solution: Echo
Echo is an agentic AI that lives on a user's smartphone, designed to see what you see, hear what you hear, and remember your experiences to provide timely, contextual help. It functions as a second brain, connecting disparate moments to offer assistance at the precise moment it's needed, without ever being asked.

### User Journey Example:
*   **The Setup:** A user is assembling a bookshelf and realizes they are missing a specific type of screw. They go to the hardware store and, while looking at various options, take a quick photo of the correct screw. Echo, running silently in the background, sees this image. It uses its on-device vision tool to identify the object and logs it to its private memory stream: `{"event": "image_capture", "timestamp": "14:32", "content": "object: screw, type: wood, head: flat, size: 1.5-inch"}`.
*   **The Contextual Failure:** An hour later, back at home, the user is looking at the partially assembled bookshelf, visibly stuck. They have a handful of the wrong screws in their hand.
*   **The Proactive Assistance:** Echo, through the phone's camera, perceives the context: the bookshelf, the screws, and the user's long pause. It queries its memory for relevant recent events. It finds the memory of the screw from the hardware store and connects it to the current situation.
*   **The Novel Interaction:** Instead of an intrusive pop-up, the phone gives a gentle haptic buzz. The user glances at the lock screen, which now displays a simple, contextual notification: "Still working on the bookshelf? Remember the 1.5-inch flat-head screws you saw at the store? That might be what you need here."

## 5. Technical Implementation & Documentation
Our architecture is built on a continuous, on-device agentic loop.

*   **Architecture: The Perceive-Reason-Act Loop**
    1.  **Perceive:** Echo's sensory tools (`VisionTool`, `AudioTool`) constantly and efficiently process the environment, creating structured log entries in the on-device `MemoryStream`.
    2.  **Reason:** The core agent, powered by an on-device LLM like Gemma 3n, periodically reviews the current context and queries the `MemoryStream`. It runs a "relevance check" to see if past memories can help with the present situation.
    3.  **Act:** If the reasoning core finds a high-probability connection, it formulates a suggestion and chooses the least intrusive way to deliver it via the `NotificationTool`.

*   **Components:**
    *   `VisionTool`: An on-device computer vision model (e.g., a quantized MobileNetV3) that performs object recognition and scene classification on the camera feed.
    *   `AudioTool`: An on-device audio processing model that can transcribe short snippets of speech or identify significant environmental sounds (e.g., alarms, sirens).
    *   `MemoryStream`: A local vector database (e.g., using SQLite with a vector extension) that stores the structured outputs from the sensory tools. This allows for efficient semantic search over the user's experiences.
    *   **Reasoning Core:** The Gemma 3n model, running on-device, which synthesizes the data from the tools and memory to generate helpful, natural language suggestions.

## 6. UI/UX Design & Human-AI Interaction
The core of Echo's H-AI model is **proactive subtlety**. We are explicitly designing against the "annoying assistant" trope.
*   **No Primary UI:** Echo has no app icon or main screen. Its presence is felt only when it has something genuinely useful to contribute.
*   **Graduated Notifications:** The interaction model is context-aware.
    *   **Low Priority:** A simple, dynamic notification on the lock screen or AOD.
    *   **Medium Priority:** A gentle haptic buzz on a phone or connected smartwatch.
    *   **High Priority (User-defined):** An auditory suggestion, e.g., "You left your wallet on the coffee table."
*   **Implicit Control:** The user controls Echo by their actions. Dismissing a notification teaches the agent that the suggestion was not helpful in that context, refining its reasoning loop for the future.

## 7. Ethical Considerations & Scalability
*   **Ethics & Privacy by Design:** This is the cornerstone of our project. Echo is **100% on-device**. No user data—no images, no audio, no memories—ever leaves the phone. All processing, including the LLM reasoning, happens locally. This makes Echo fundamentally more private and secure than any cloud-based assistant. The user has full control to pause the agent or wipe its memory at any time.
*   **Scalability:** The agent scales with the user. To manage storage, the `MemoryStream` will use an auto-summarization strategy. At the end of each day, the agent will use the LLM to create a summary of the day's events, compressing detailed logs into more abstract memories, thus preserving knowledge while conserving space.

## 8. Demo Video Plan
The 2-minute video will tell a clear, human-centric story.

*   **Scene 1 (0:00-0:30):** A shot of our user, Sarah, looking at a recipe on her phone in a busy grocery store. She picks up a bottle of soy sauce.
    *   *On-screen text:* "Echo sees your world, privately noting key items in its on-device memory."
    *   *Visual:* A small, transparent overlay shows the data point being created: `[item: soy sauce]`.
*   **Scene 2 (0:30-1:00):** Sarah is at home in her kitchen, starting to cook. She looks through her pantry with a puzzled expression.
    *   *On-screen text:* "Later, Echo understands your context..."
*   **Scene 3 (1:00-1:30):** A simple, clean animation shows Echo's agentic loop:
    1.  `Context: "User is in kitchen"`
    2.  `Memory Query: "groceries"`
    3.  `Result: "soy sauce"`
    4.  `Reasoning: "User might be looking for the soy sauce they just bought."`
*   **Scene 4 (1:30-2:00):** Sarah glances at her phone. A simple, elegant notification appears: "The soy sauce is likely in the grocery bag on the counter." She smiles, relieved.
    *   *Final Title Card:* "Echo. Your Untethered AI Companion. Private. Proactive. On-Device."
