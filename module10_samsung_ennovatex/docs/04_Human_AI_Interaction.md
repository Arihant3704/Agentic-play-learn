# 4. Human-AI Interaction (H-AI) Model

The interaction model for Echo is designed to be **implicit and proactive**, a direct contrast to the explicit, command-based nature of traditional assistants.

## 4.1. Core Principle: Graduated Subtlety
Echo understands that not all information is equally important. It uses a system of graduated notifications to deliver suggestions without causing unnecessary distraction.

-   **Level 1: Information (Silent & Ambient):** For low-priority but potentially useful information (e.g., "You bought soy sauce earlier"), the suggestion might appear on an always-on display or as a dynamic lock-screen widget. It's there if the user glances at it, but doesn't demand attention.
-   **Level 2: Suggestion (Haptic & Gentle):** For medium-priority suggestions where the user might want to take an action (e.g., "Your wallet is on the table"), the agent will provide a gentle haptic buzz on the user's phone or smartwatch. This prompts the user to look at the device for the suggestion.
-   **Level 3: Alert (Auditory & Explicit):** For high-priority, critical safety events (e.g., a smoke alarm), the agent will use an auditory alert and a clear, spoken message to ensure it gets the user's immediate attention.

## 4.2. Learning from Interaction
The user teaches Echo through their natural behavior.
-   **Positive Reinforcement:** If Echo suggests looking for the soy sauce and the user immediately picks it up, this confirms the suggestion was helpful. The agent can log this as a successful interaction.
-   **Negative Reinforcement:** If Echo provides a suggestion and the user dismisses the notification or ignores it, the agent learns that this type of suggestion, in this context, was not useful. This feedback helps to refine the `ReasoningCore` over time, making the agent less intrusive and more genuinely helpful.

This H-AI model makes the agent feel less like a piece of software and more like a thoughtful companion that understands social cues.
