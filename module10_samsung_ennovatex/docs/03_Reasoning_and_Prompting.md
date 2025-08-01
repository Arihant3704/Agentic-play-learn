# 3. The Reasoning Core & Prompting Strategy

The `DecisionAgent` is the LLM-powered reasoning core of Echo. Its effectiveness hinges on its ability to synthesize complex, multi-modal information into actionable insights.

## 3.1. The Role of the LLM (within `DecisionAgent`)
The LLM receives a highly structured, text-based summary of the agent's current perception (from the `PerceptionAgent`) and relevant memories (from the `MemoryStream`). Its role is to perform high-level cognitive tasks:
-   **Contextual Understanding:** Interpreting the VLM-like scene descriptions.
-   **Intent Inference:** Deducing user needs or potential issues based on observations and memories.
-   **Action Selection:** Deciding whether to provide a suggestion or issue a direct control command.
-   **Prioritization:** Ensuring critical alerts (like safety) take precedence.

## 3.2. The Master Prompt Template
Our `DecisionAgent` uses a dynamic master prompt that leverages the richer input from the `PerceptionAgent`.

```text
You are Echo, a proactive AI companion. Your goal is to be helpful without being intrusive. You can either suggest advice as text, or you can issue a command to control a device. Commands must be in the format: ACTION: tool_name.method('parameter'). If no action or advice is needed, respond with only the word "None".

--- DATA START ---
**Current Visual Scene Description:** {{scene_description}}
**Objects Detected:** {{list_of_objects}}
**Ambient Sound Detected:** {{sound_description}}
**Recent Relevant Memories (Semantic Search Results):**
{{memory_items}}
--- DATA END ---

Based *only* on the data above, what is your suggestion or action?
Response: 
"""

## 3.3. Example Walkthrough (Enhanced)
-   **Scenario:** User is in the kitchen, and a smoke alarm is beeping. The `PerceptionAgent` provides a detailed scene description.
-   **Data fed to prompt:**
    -   `scene_description`: "User is in the kitchen, facing a counter with a cutting board, a knife, and an empty pan. There's a smoke alarm on the ceiling."
    -   `list_of_objects`: "cutting_board, knife, empty_pan, smoke_alarm"
    -   `sound_description`: "smoke_alarm_beep"
    -   `memory_items`: "- User saw soy_sauce_bottle (earlier)"
-   **Expected LLM Output:** Given the explicit mention of the smoke alarm in the scene description and the sound, the LLM will prioritize safety: `CRITICAL ALERT: A smoke alarm has been detected. Please check your kitchen immediately.`

This multi-modal, VLM-enhanced input allows the LLM to make more nuanced and accurate decisions, leading to more effective proactive assistance.