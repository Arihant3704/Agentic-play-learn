# echo_controller_template.py
# A more advanced template demonstrating the "Echo" agent controlling other applications.

import time
import random

# --- 1. Simulated Tools (Senses and Actuators) ---

class VisionTool:
    """Simulates the phone's camera."""
    def get_current_scene(self, context):
        if context == "working_late":
            return {"scene": "desk", "objects": ["laptop", "keyboard", "long_document"]}
        # ... (other contexts from before)
        elif context == "grocery_store":
            return {"scene": "grocery_aisle", "objects": ["shelf", "cans", "soy_sauce_bottle"]}
        elif context == "kitchen_cooking":
            return {"scene": "kitchen_counter", "objects": ["cutting_board", "knife", "empty_pan"]}
        elif context == "leaving_home":
            return {"scene": "doorway", "objects": ["keys", "shoes", "wallet_on_table"]}
        else:
            return {"scene": "generic", "objects": []}

class AudioTool:
    """Simulates the phone's microphone."""
    def get_ambient_sound(self):
        if random.random() < 0.1: return {"sound": "smoke_alarm_beep"}
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
    """Simulates an on-device vector database."""
    def __init__(self):
        self.memories = []
        print("MemoryStream: Initialized.")

    def add_memory(self, event_data):
        memory = {"timestamp": time.time(), "event": event_data}
        self.memories.append(memory)
        print(f"MemoryStream: Added memory - {event_data}")

# --- 2. The REAL Reasoning Core (Connects to an LLM) ---

class ReasoningCore:
    """Constructs a prompt and uses an LLM for decision-making."""
    def __init__(self):
        print("ReasoningCore: Initialized.")

    def analyze_and_suggest(self, current_scene, ambient_sound):
        prompt = self._build_prompt(current_scene, ambient_sound)
        response_text = self._simulate_llm_response(prompt)
        return response_text.strip()

    def _build_prompt(self, current_scene, ambient_sound):
        sound_str = ambient_sound.get('sound', 'None') if ambient_sound else "None"
        prompt = f"""
You are Echo, a proactive AI companion. Analyze the following data. Your goal is to be helpful. You can either suggest advice as text, or you can issue a command to control a device. Commands must be in the format: ACTION: tool_name.method('parameter'). If no action or advice is needed, respond with "None".

--- DATA START ---
**Current Visual Scene:** {current_scene.get('scene', 'unknown')}
**Objects Detected:** {', '.join(current_scene.get('objects', []))}
**Ambient Sound:** {sound_str}
--- DATA END ---

Based on the data, what is your suggestion or action?
Response: 
"""
        return prompt

    def _simulate_llm_response(self, prompt):
        if "smoke_alarm_beep" in prompt: return "CRITICAL ALERT: A smoke alarm has been detected!"
        if "wallet_on_table" in prompt: return "Just a heads-up, your wallet is still on the table."
        if "long_document" in prompt and "desk" in prompt:
            return "ACTION: music_player.play('deep_focus')"
        return "None"

# --- 3. The Echo Agent (Orchestrator) ---

class EchoAgent:
    def __init__(self):
        print("--- Echo Agent Initializing ---")
        self.vision = VisionTool()
        self.audio = AudioTool()
        self.memory = MemoryStream()
        self.reasoning = ReasoningCore()
        self.music_player = MusicPlayer()
        self.context = "idle"
        print("--- Echo Agent Ready ---\n")

    def set_context(self, new_context):
        print(f"--- CONTEXT CHANGE: User is now `{new_context}` ---")
        self.context = new_context

    def execute_action(self, action_string):
        print(f"EchoAgent: Received command - {action_string}")
        try:
            # Simple parser for "tool.method('parameter')"
            target, call = action_string.split('.')
            method, param = call.split('(')
            param = param.strip("')").strip()

            if target == "music_player":
                if method == "play":
                    self.music_player.play(param)
                else:
                    print(f"EchoAgent: Unknown method '{method}' for MusicPlayer.")
            else:
                print(f"EchoAgent: Unknown tool '{target}'.")
        except Exception as e:
            print(f"EchoAgent: Failed to execute action '{action_string}'. Error: {e}")

    def run_perceptive_loop(self, force_audio_event=False):
        print(f"\n--- Running Agentic Loop (Time: {int(time.time())}) ---")
        current_scene = self.vision.get_current_scene(self.context)
        print(f"VisionTool: Sees `{current_scene['scene']}` with objects: {current_scene['objects']}")
        
        ambient_sound = self.audio.get_ambient_sound()
        if force_audio_event: ambient_sound = {"sound": "smoke_alarm_beep"}
        if ambient_sound: print(f"AudioTool: Heard `{ambient_sound['sound']}`")

        suggestion_or_action = self.reasoning.analyze_and_suggest(current_scene, ambient_sound)

        if suggestion_or_action.startswith("ACTION:"):
            command = suggestion_or_action.split("ACTION:")[1].strip()
            self.execute_action(command)
        elif suggestion_or_action != "None":
            print(f"\n>>> ECHO (Proactive Suggestion): {suggestion_or_action}\n")
        else:
            print("ReasoningCore: No action or suggestion needed.")

# --- 4. Main Simulation ---

if __name__ == "__main__":
    agent = EchoAgent()

    agent.set_context("leaving_home")
    agent.run_perceptive_loop()
    time.sleep(1)

    print("\n*** SIMULATING A WORK SCENARIO ***")
    agent.set_context("working_late")
    agent.run_perceptive_loop() # This should trigger the agent to take control
