import random

class NPC:
    def __init__(self, name, personality_traits):
        self.name = name
        self.personality_traits = personality_traits # e.g., ['brave', 'curious', 'timid']
        self.current_state = "idle"
        self.memory = []

    def perceive_environment(self, environment_data):
        # In a real engine, this would involve complex sensory input
        # For this example, we simulate perception based on simple data
        perceived_threat = environment_data.get('threat', False)
        perceived_opportunity = environment_data.get('opportunity', False)
        return {"threat": perceived_threat, "opportunity": perceived_opportunity}

    def decide_action(self, perception):
        # AI-driven decision making based on traits and perception
        if perception['threat'] and 'brave' not in self.personality_traits:
            self.current_state = "flee"
        elif perception['opportunity'] and 'curious' in self.personality_traits:
            self.current_state = "investigate"
        elif 'timid' in self.personality_traits and random.random() < 0.3:
            self.current_state = "hide"
        else:
            self.current_state = "idle"

        self.memory.append((self.current_state, perception))
        return self.current_state

    def execute_action(self):
        # In a real engine, this would trigger animations, movement, etc.
        print(f"{self.name} is now {self.current_state}.")

# --- Simulation Setup ---

# Define NPCs with different personality traits
npc1 = NPC("Geralt", ["brave", "curious"])
npc2 = NPC("Yennefer", ["curious", "intelligent"])
npc3 = NPC("Ciri", ["timid", "brave"])

npcs = [npc1, npc2, npc3]

# Simulate environmental changes
environments = [
    {"threat": False, "opportunity": False}, # Calm
    {"threat": True, "opportunity": False},  # Danger
    {"threat": False, "opportunity": True},   # Interesting discovery
    {"threat": True, "opportunity": True}    # Mixed situation
]

print("--- Starting AI NPC Behavior Simulation ---")

for i, env in enumerate(environments):
    print(f"\n--- Environment {i+1}: {env} ---")
    for npc in npcs:
        perception = npc.perceive_environment(env)
        action = npc.decide_action(perception)
        npc.execute_action()

print("\n--- Simulation Complete ---")
