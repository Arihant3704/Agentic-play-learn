# echo_multi_agent_template.py
# A more advanced template demonstrating the "Echo" agent with VLM-like perception
# and a conceptual multi-agent architecture.

import time
import random

# --- 1. Specialized Agents/Tools ---

class VisionTool:
    """Simulates the phone's camera and provides VLM-like scene descriptions."""
    def analyze_frame(self, context):
        """Analyzes a single frame to identify objects or scenes based on context."""
        # In a real application, this would process a real camera frame
        # and use a VLM to generate the description and objects.
        if context == "grocery_store":
            return {"scene_description": "User is in a grocery aisle, looking at shelves with various canned goods and a distinct soy sauce bottle.", "objects": ["shelf", "cans", "soy_sauce_bottle"]}
        elif context == "kitchen_cooking":
            return {"scene_description": "User is in the kitchen, facing a counter with a cutting board, a knife, and an empty pan. There's a smoke alarm on the ceiling.", "objects": ["cutting_board", "knife", "empty_pan", "smoke_alarm"]}
        elif context == "leaving_home":
            return {"scene_description": "User is near the doorway. Keys are on a hook, shoes are by the door, and a wallet is visible on a nearby table.", "objects": ["keys", "shoes", "wallet_on_table"]}
        elif context == "working_late":
            return {"scene_description": "User is at a desk, looking at a laptop with a long document open. A keyboard is in front of them.", "objects": ["laptop", "keyboard", "long_document"]}
        else:
            return {"scene_description": "User is in a generic environment.", "objects": []}

class AudioTool:
    """Simulates the phone's microphone."""
    def get_ambient_sound(self, force_event=False):
        if force_event or random.random() < 0.01: 
            return {"sound": "smoke_alarm_beep"}
        return None

class MusicPlayer:
    """Simulates a controllable music application."""
    def __init__(self):
        self.status = "stopped"
        self.current_playlist = None
        print("MusicPlayer: Initialized.")

    def play(self, playlist):
        self.status = "playing"
        self.current_playlist = playlist
        print(f"MusicPlayer: ACTION - Now playing the '{self.current_playlist}' playlist.")

class MemoryStream:
    """Simulates an on-device vector database for storing and retrieving memories."""
    def __init__(self):
        self.memories = []
        print("MemoryStream: Initialized.")

    def add_memory(self, event_data):
        memory = {"timestamp": time.time(), "event": event_data}
        self.memories.append(memory)
        # print(f"MemoryStream: Added memory - {event_data}") # Too verbose for real-time

    def search_related_memories(self, keywords):
        related = [m for m in self.memories if any(keyword in str(m['event']) for keyword in keywords)]
        return related

# --- 2. Multi-Agent Components ---

class PerceptionAgent:
    """Coordinates sensory input and provides structured observations."""
    def __init__(self, vision_tool, audio_tool):
        self.vision_tool = vision_tool
        self.audio_tool = audio_tool

    def get_observations(self, context, force_audio_event=False):
        # Always analyze vision when called in this simulation for clear demonstration
        current_scene_data = self.vision_tool.analyze_frame(context)
        
        ambient_sound = self.audio_tool.get_ambient_sound(force_event=force_audio_event)

        return current_scene_data, ambient_sound

class DecisionAgent:
    """Acts as the LLM-powered reasoning core, making suggestions or issuing actions."""
    def __init__(self):
        print("DecisionAgent: Initialized. (LLM-powered reasoning)")

    def analyze_and_decide(self, scene_data, recent_memories, ambient_sound):
        # Prioritize critical, current sensory input
        if ambient_sound and ambient_sound.get('sound') == "smoke_alarm_beep":
            return "CRITICAL ALERT: A smoke alarm has been detected. Please check your kitchen immediately."

        prompt = self._build_prompt(scene_data, recent_memories, ambient_sound)
        response_text = self._simulate_llm_response(prompt)
        return response_text.strip()

    def _build_prompt(self, scene_data, recent_memories, ambient_sound):
        memories_str = "\n".join([f"- {m['event']}" for m in recent_memories]) if recent_memories else "None"
        sound_str = ambient_sound.get('sound', 'None') if ambient_sound else "None"
        
        prompt = f"""
You are Echo, a proactive AI companion. Your goal is to be helpful without being intrusive. You can either suggest advice as text, or you can issue a command to control a device. Commands must be in the format: ACTION: tool_name.method('parameter'). If no action or advice is needed, respond with only the word "None".

--- DATA START ---
**Current Visual Scene Description:** {scene_data.get('scene_description', 'unknown')}
**Objects Detected:** {', '.join(scene_data.get('objects', []))}
**Ambient Sound:** {sound_str}
**Recent Relevant Memories:**
{memories_str}
--- DATA END ---

Based *only* on the data above, what is your suggestion or action?
Response: 
"""
        return prompt

    def _simulate_llm_response(self, prompt):
        # This function simulates the behavior of a well-instructed LLM.
        # Note: Critical alerts are handled *before* this function in analyze_and_decide
        if "long_document" in prompt and "desk" in prompt:
            return "ACTION: music_player.play('deep_focus')"
        if "wallet_on_table" in prompt:
            return "Just a heads-up, your wallet is still on the table."
        if "kitchen_cooking" in prompt and "soy_sauce_bottle" in prompt:
            return "You just bought soy sauce. Are you looking for it to start cooking?"
        return "None"

class ActionAgent:
    """Executes commands issued by the DecisionAgent."""
    def __init__(self, music_player):
        self.music_player = music_player

    def execute_command(self, action_string):
        print(f"ActionAgent: Executing command - {action_string}")
        try:
            target, call = action_string.split('.')
            method, param = call.split('(')
            param = param.strip("')").strip()

            if target == "music_player":
                if method == "play":
                    self.music_player.play(param)
                else:
                    print(f"ActionAgent: Unknown method '{method}' for MusicPlayer.")
            else:
                print(f"ActionAgent: Unknown tool '{target}'.")
        except Exception as e:
            print(f"ActionAgent: Failed to execute action '{action_string}'. Error: {e}")

# --- 3. The Echo Agent (Orchestrator/Control Plane) ---

class EchoAgent:
    def __init__(self):
        print("--- Echo Agent (Orchestrator) Initializing ---")
        self.music_player = MusicPlayer()
        self.memory_stream = MemoryStream()
        
        # Initialize specialized agents
        self.perception_agent = PerceptionAgent(VisionTool(), AudioTool())
        self.decision_agent = DecisionAgent()
        self.action_agent = ActionAgent(self.music_player)

        self.context = "idle" # Context is now derived from VisionTool
        self.last_suggestion = ""
        print("--- Echo Agent Ready ---\n")

    def set_context(self, new_context):
        print(f"--- CONTEXT CHANGE: User is now in `{new_context}` ---")
        self.context = new_context

    def run_multi_agent_loop(self, force_audio_event=False):
        print(f"\n--- Running Multi-Agent Loop (Time: {int(time.time())}) ---")
        
        # 1. Perception Agent gathers observations
        current_scene_data, ambient_sound = self.perception_agent.get_observations(self.context, force_audio_event)

        if current_scene_data: # Always true now that VisionTool doesn't have interval
            print(f"PerceptionAgent: Observed: {current_scene_data['scene_description']}")
            
            # Memory Agent (integrated into orchestrator for simplicity here) adds to stream
            self.memory_stream.add_memory({'type': 'visual_description', 'content': current_scene_data['scene_description']})
            if "soy_sauce_bottle" in current_scene_data['objects']:
                self.memory_stream.add_memory({'type': 'visual_object', 'content': 'User saw soy_sauce_bottle'})

            if ambient_sound:
                print(f"PerceptionAgent: Heard `{ambient_sound['sound']}`")
                self.memory_stream.add_memory({'type': 'audio_event', 'content': ambient_sound['sound']})

            # 2. Decision Agent analyzes and decides
            recent_memories = self.memory_stream.search_related_memories(["soy_sauce", "wallet", "smoke_alarm", "focus"])
            suggestion_or_action = self.decision_agent.analyze_and_decide(current_scene_data, recent_memories, ambient_sound)

            # 3. Orchestrator directs Action Agent or provides suggestion
            if suggestion_or_action.startswith("ACTION:"):
                command = suggestion_or_action.split("ACTION:")[1].strip()
                self.action_agent.execute_command(command)
                self.last_suggestion = f"ACTION: {command}"
            elif suggestion_or_action != "None":
                self.last_suggestion = suggestion_or_action
                print(f"\n>>> ECHO (Proactive Suggestion): {self.last_suggestion}\n")
            else:
                self.last_suggestion = "No suggestion/action."
                print("DecisionAgent: No action or suggestion needed.")
        else:
            # This branch should ideally not be hit with the current VisionTool setup
            self.last_suggestion = "No new visual data for analysis."
            print("PerceptionAgent: No new visual data for analysis.")
        
        return self.last_suggestion

# --- 4. Main Simulation ---

if __name__ == "__main__":
    agent = EchoAgent()

    # Simulate the user's day with different contexts
    agent.set_context("grocery_store")
    agent.run_multi_agent_loop()
    time.sleep(1)

    agent.set_context("kitchen_cooking")
    agent.run_multi_agent_loop() 
    time.sleep(1)

    print("\n*** SIMULATING A CRITICAL SAFETY EVENT ***")
    agent.set_context("kitchen_cooking")
    agent.run_multi_agent_loop(force_audio_event=True) # Force the smoke alarm sound
    time.sleep(1)

    agent.set_context("leaving_home")
    agent.run_multi_agent_loop()
    time.sleep(1)

    print("\n*** SIMULATING A WORK SCENARIO (VLM-triggered action) ***")
    agent.set_context("working_late")
    agent.run_multi_agent_loop()
    time.sleep(1)
