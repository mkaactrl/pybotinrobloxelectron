import pyautogui
import time
import random

# Function to dynamically generate combat responses based on attack type
def generate_retaliation(attack_type):
    # Elements of the retaliation (actions, effects, and powerups)
    attack_actions = [
        "phases across the multiverse to counter your attack",
        "summons energy from a trillion dimensions to obliterate you",
        "collapses the fabric of time itself with a single thought",
        "unleashes a cosmic burst that splits reality in half",
        "flicks a finger and distorts the fundamental laws of physics"
    ]
    
    attack_effects = [
        "causing the collapse of countless universes",
        "leaving entire realities trembling in fear",
        "creating a singularity that devours everything in its path",
        "shattering the very essence of existence itself",
        "ripping through the boundaries of spacetime with each strike"
    ]
    
    attack_intensities = [
        "with a force that reverberates across countless dimensions",
        "so powerful that it warps the nature of reality itself",
        "with an intensity that obliterates entire timelines",
        "so swift that time itself struggles to keep up",
        "that creates a shockwave across infinite universes"
    ]
    
    # Map attacks to specific retaliation actions
    attack_responses = {
        "punching": f"You dare punch me? {random.choice(attack_actions)} {random.choice(attack_effects)} {random.choice(attack_intensities)}!",
        "slamming": f"You slam me into the void? {random.choice(attack_actions)} {random.choice(attack_effects)} {random.choice(attack_intensities)}!",
        "kicking": f"You think your kick can hurt me? {random.choice(attack_actions)} {random.choice(attack_effects)} {random.choice(attack_intensities)}!",
        "throwing": f"You throw me? You just sealed your own fate! {random.choice(attack_actions)} {random.choice(attack_effects)} {random.choice(attack_intensities)}!",
        "attacking": f"Your attack is futile! I transcend your feeble attempt with a counter so powerful that {random.choice(attack_effects)} {random.choice(attack_intensities)}!"
    }

    # If the attack type is recognized, generate the response
    if attack_type in attack_responses:
        return attack_responses[attack_type]
    
    # If attack type is unknown, return a generic response
    return f"You dare attack me? I will end you across all planes of existence. Prepare for your annihilation!"

# Function to simulate typing at 350 WPM (around 0.17 seconds per character)
def type_text_at_350_wpm(text):
    time_per_char = 0.17  # Adjust this delay to match 350 WPM
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(time_per_char)

# Function to handle player attack detection and response generation
def on_player_attack(player_message):
    # Keywords for different attack actions
    attack_keywords = {
        "punching": "punching",
        "slamming": "slamming",
        "kicking": "kicking",
        "throwing": "throwing",
        "attack": "attacking"
    }
    
    # Check if any of the attack keywords are in the player's message
    for attack_keyword, attack_type in attack_keywords.items():
        if attack_keyword in player_message.lower():
            # Generate the bot's retaliation response
            response = generate_retaliation(attack_type)
            print(f"Bot is typing: {response}")
            
            # Open chat window (assume 'T' opens chat in Roblox)
            pyautogui.press('t')
            time.sleep(0.5)  # Wait for the chat window to open
            
            # Type the retaliation response at 350 WPM
            type_text_at_350_wpm(response)
            
            # Send the message by pressing 'Enter'
            pyautogui.press('enter')
            break

# Simulate receiving a player's attack message (for testing purposes)
while True:
    # Simulate player input for testing
    player_message = input("Player's attack message: ")

    # Bot reacts when an attack is detected
    on_player_attack(player_message)
    
    # Wait before detecting the next possible attack
    time.sleep(1)  # Adjust this delay if necessary
