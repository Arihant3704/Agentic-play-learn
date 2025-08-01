# realtime_camera_agent.py
# Connects to a phone's IP camera stream and processes it with a simulated agent.
# This version integrates the agent's reasoning and control capabilities.

import cv2
import numpy as np
import time
import random

# --- 1. Simulated Tools (Senses and Actuators) ---

class VisionTool:
    """Simulates the phone's camera and provides mock environmental data based on color."""
    def __init__(self):
        self.last_analysis_time = time.time()
        self.analysis_interval = 3 # seconds

    def analyze_frame(self, frame):
        """Analyzes a single frame to identify objects or scenes based on color."""
        if time.time() - self.last_analysis_time < self.analysis_interval:
            return None # Only analyze every few seconds for performance

        self.last_analysis_time = time.time()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Simple color detection to simulate different contexts
        # Red for kitchen/soy sauce
        lower_red1 = np.array([0, 120, 70]); upper_red1 = np.array([10, 255, 255])
        lower_red2 = np.array([170, 120, 70]); upper_red2 = np.array([180, 255, 255])
        mask_red = cv2.inRange(hsv, lower_red1, upper_red1) + cv2.inRange(hsv, lower_red2, upper_red2)
        red_pixels = np.sum(mask_red > 0)

        # Blue for leaving home/wallet
        lower_blue = np.array([90, 50, 50]); upper_blue = np.array([130, 255, 255])
        mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
        blue_pixels = np.sum(mask_blue > 0)

        # Green for working late/focus
        lower_green = np.array([40, 40, 40]); upper_green = np.array([80, 255, 255])
        mask_green = cv2.inRange(hsv, lower_green, upper_green)
        green_pixels = np.sum(mask_green > 0)

        # Determine context based on dominant color
        if red_pixels > 10000: # Threshold for significant color presence
            return {"scene": "kitchen_cooking", "objects": ["cutting_board", "knife", "empty_pan", "soy_sauce_bottle"]}
        elif blue_pixels > 10000:
            return {"scene": "leaving_home", "objects": ["keys", "shoes", "wallet_on_table"]}
        elif green_pixels > 10000:
            return {"scene": "working_late", "objects": ["laptop", "keyboard", "long_document"]}
        else:
            return {"scene": "generic", "objects": []}

class AudioTool:
    """Simulates the phone's microphone."""
    def get_ambient_sound(self):
        # In a real app, this would use a real-time audio processing model.
        # For simulation, we can randomly trigger a safety event.
        if random.random() < 0.01: # Very low chance to trigger randomly
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

# --- 2. The REAL Reasoning Core (Connects to an LLM) ---

class ReasoningCore:
    """Constructs a prompt and uses an LLM for decision-making."""
    def __init__(self):
        # In a real app, you would initialize your LLM client here.
        # from some_llm_library import GemmaClient
        # self.llm_client = GemmaClient(api_key="YOUR_API_KEY")
        print("ReasoningCore: Initialized. (Ready to connect to LLM)")

    def analyze_and_suggest(self, current_scene, recent_memories, ambient_sound):
        prompt = self._build_prompt(current_scene, recent_memories, ambient_sound)
        response_text = self._simulate_llm_response(prompt)
        return response_text.strip()

    def _build_prompt(self, current_scene, recent_memories, ambient_sound):
        memories_str = "\n".join([f"- {m['event']}" for m in recent_memories]) if recent_memories else "None"
        sound_str = ambient_sound.get('sound', 'None') if ambient_sound else "None"
        
        prompt = f"""
You are Echo, a proactive AI companion. Your goal is to be helpful without being intrusive. You can either suggest advice as text, or you can issue a command to control a device. Commands must be in the format: ACTION: tool_name.method('parameter'). If no action or advice is needed, respond with "None".

--- DATA START ---
**Current Visual Scene:** {current_scene.get('scene', 'unknown')}
**Objects Detected:** {', '.join(current_scene.get('objects', []))}
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
        # The order here matters for prioritization (e.g., safety first).
        if "smoke_alarm_beep" in prompt:
            return "CRITICAL ALERT: A smoke alarm has been detected. Please check your kitchen immediately."
        if "long_document" in prompt and "desk" in prompt:
            return "ACTION: music_player.play('deep_focus')"
        if "wallet_on_table" in prompt:
            return "Just a heads-up, your wallet is still on the table."
        if "kitchen_cooking" in prompt and "soy_sauce_bottle" in prompt:
            return "You just bought soy sauce. Are you looking for it to start cooking?"
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
        self.context = "idle" # Context is now derived from VisionTool
        self.last_suggestion = ""
        print("--- Echo Agent Ready ---\n")

    def execute_action(self, action_string):
        print(f"EchoAgent: Executing command - {action_string}")
        try:
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

    def run_perceptive_loop(self, frame):
        # 1. Perceive the environment
        current_scene_data = self.vision.analyze_frame(frame)
        ambient_sound = self.audio.get_ambient_sound()

        if current_scene_data: # Only run reasoning if vision tool provides new data
            self.context = current_scene_data['scene'] # Update context based on vision
            # print(f"VisionTool: Sees `{self.context}` with objects: {current_scene_data['objects']}")
            
            # Add significant visual events to memory (e.g., if soy sauce bottle is seen)
            if "soy_sauce_bottle" in current_scene_data['objects']:
                self.memory.add_memory({'type': 'visual', 'content': 'User saw soy_sauce'})

            if ambient_sound:
                # print(f"AudioTool: Heard `{ambient_sound['sound']}`")
                self.memory.add_memory({'type': 'audio', 'content': ambient_sound['sound']})

            recent_memories = self.memory.search_related_memories(["saw", "heard"])
            suggestion_or_action = self.reasoning.analyze_and_suggest(current_scene_data, recent_memories, ambient_sound)

            if suggestion_or_action.startswith("ACTION:"):
                command = suggestion_or_action.split("ACTION:")[1].strip()
                self.execute_action(command)
                self.last_suggestion = f"ACTION: {command}"
            elif suggestion_or_action != "None":
                self.last_suggestion = suggestion_or_action
            else:
                self.last_suggestion = "No suggestion."
        
        return self.last_suggestion

# --- Main Application Logic ---

def main():
    print("--- Real-Time Agent with Control Initializing ---")
    print("1. Start the IP Webcam app on your phone.")
    print("2. Enter the full video feed URL provided by the app.")
    print("   (e.g., http://192.168.1.10:8080/video)")
    print("3. Hold up RED, BLUE, or GREEN objects to your camera to trigger scenarios.")
    print("4. Press 'q' to quit.")
    
    # Hardcode the URL here to avoid interactive input
    url = "http://10.4.0.205:8080/video"

    if not url:
        print("No URL entered. Exiting.")
        return

    cap = cv2.VideoCapture(url)

    if not cap.isOpened():
        print("Error: Could not connect to the camera stream.")
        print("Please check the URL and ensure your phone and computer are on the same WiFi network.")
        return

    print("Successfully connected to camera. Starting agent...")
    agent = EchoAgent()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to grab frame from the stream. Exiting.")
            break

        frame = cv2.resize(frame, (640, 480))

        # Run the agent's perceptive loop and get its last output
        agent_output = agent.run_perceptive_loop(frame)

        # Display the agent's output on the frame
        cv2.putText(frame, f"Agent: {agent_output}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.imshow('Real-Time Echo Agent', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Stream stopped. Agent shut down.")

if __name__ == "__main__":
    main()