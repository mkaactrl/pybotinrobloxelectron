import pyautogui
import time
import random

# Function to dynamically generate combat responses based on attack type
def generate_retaliation(attack_type):
    attack_responses = {
        "punching": "You think your punch can harm me? I'll counter with a barrage of lightning-fast strikes!",
        "slamming": "Slamming me? How about I teleport behind you and land a crushing blow that breaks the ground!",
        "kicking": "Your kick is no match for my reflexes! I'll dodge and strike you with a devastating combo!",
        "throwing": "Throwing me? That's a mistake! I'll phase through and land a powerful energy blast right at you!",
        "attacking": "Such a feeble attack! I respond with a ground-shaking energy wave that will leave you stunned!"
    }

    # If the attack type is recognized, generate the response
    if attack_type in attack_responses:
        return attack_responses[attack_type]
    
    # If attack type is unknown, return a generic response
    return f"You're attacking me? You won't get away with that! Prepare for my retaliation!"

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
