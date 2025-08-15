import os
import time
import itertools
import json
import sys
import random
from colorama import Fore, Style, init

# Initialize colorama for automatic style resetting
init(autoreset=True)

# Define the core ASCII art. Using raw string r"""...""" to avoid issues with backslashes.
ASCII_ART = r"""
      ██████╗ ██╗███████╗ ██████╗  ██████╗ ████████╗    ██████╗  ███████╗
     ██╔═══██╗██║██╔════╝██╔═══██╗██╔═══██╗╚══██╔══╝    ██╔══██╗ ██╔════╝
     ██║   ██║██║███████╗██║   ██║██║   ██║   ██║       ██████╔╝ █████╗  
     ██║   ██║██║╚════██║██║   ██║██║   ██║   ██║       ██╔══██╗ ██╔══╝  
     ╚██████╔╝██║███████║╚██████╔╝╚██████╔╝   ██║       ██║  ██║ ███████╗
      ╚═════╝ ╚═╝╚══════╝ ╚═════╝  ╚═════╝    ╚═╝       ╚═╝  ╚═╝ ╚══════╝
"""
SUB_TEXT = "                 SELF-BOT  SUITE V2.0"

def clear_console():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_animated_header(token_count):
    """Prints a styled, animated header with a glitch effect."""
    colors = [Fore.MAGENTA, Fore.RED, Fore.BLUE, Fore.BLACK]
    
    # Glitch animation loop
    for _ in range(10):
        clear_console()
        glitched_art = ""
        for char in ASCII_ART:
            if random.randint(0, 100) > 95:  # 5% chance to glitch a character
                glitched_art += random.choice(["#", "!", "*", "$"])
            else:
                glitched_art += char
        
        print(random.choice(colors) + glitched_art)
        print(Fore.MAGENTA + SUB_TEXT)
        time.sleep(0.06)

    # Final, stable header
    clear_console()
    print(Fore.MAGENTA + ASCII_ART)
    print(Fore.MAGENTA + SUB_TEXT)
    print(Fore.MAGENTA + "======================================================================")
    print(f"{Fore.RED} [!] WARNING: This is a frenzy tool. Self-bots violate Discord's ToS.")
    print(f"{Fore.BLUE} [+] STATUS: Loaded {token_count} tokens. The system is armed.")
    print(Fore.MAGENTA + "======================================================================")

def print_options_menu():
    """Prints the exaggerated, two-column menu of options."""
    options = [
        "Server Annihilation", "Webhook Raid", "Mass DM Assault", 
        "VC Connection Flooder", "Friend Request Spam", "Profile Cycler",
        "Guild Cloner", "Mass Server Leave", "Nitro Code Sniper",
        "Vanity URL Sniper", "Username Tracker", "RPC Controller",
        "Token Validator", "System Purge"
    ]

    midpoint = (len(options) + 1) // 2
    
    print(Fore.MAGENTA + "╔" + "═" * 36 + "╦" + "═" * 37 + "╗")
    print(Fore.MAGENTA + f"║{'AVAILABLE COMMAND MODULES':^74}║")
    print(Fore.MAGENTA + "╠" + "═" * 36 + "╬" + "═" * 37 + "╣")

    for i in range(midpoint):
        left_opt = f"  [{i+1}] {options[i]}"
        
        right_index = i + midpoint
        if right_index < len(options):
            right_opt = f"  [{right_index+1}] {options[right_index]}"
        else:
            right_opt = ""
            
        print(f"{Fore.MAGENTA}║ {Fore.BLUE}{left_opt:<34} {Fore.MAGENTA}║ {Fore.BLUE}{right_opt:<35} {Fore.MAGENTA}║")

    print(Fore.MAGENTA + "╚" + "═" * 36 + "╩" + "═" * 37 + "╝")

def animate_loading(text="Processing", duration=2):
    """Shows a simple loading animation with the new color palette."""
    chars = itertools.cycle(['>--', '->-', '-->'])
    start_time = time.time()
    while time.time() - start_time < duration:
        sys.stdout.write(f'\r{Fore.BLUE}{text}... {Fore.MAGENTA}{next(chars)}')
        sys.stdout.flush()
        time.sleep(0.2)
    print(f'\r{Fore.MAGENTA}{text}... System Ready.          ')

def generate_config_interactive():
    """Interactively generate the configuration file with the new color scheme."""
    clear_console()
    print(f"\n{Fore.MAGENTA}--- SYSTEM CONFIGURATION REQUIRED ---")
    print(f"{Fore.RED}No 'config.json' found. Initializing setup protocol.")
    
    config = {}
    
    # Use blue for prompts, white for user input for readability
    prompt_color = Fore.BLUE
    input_color = Style.BRIGHT + Fore.WHITE 
    
    # Core
    config['prefix'] = input(f"{prompt_color} > Enter command prefix (e.g., .): {input_color}") or "."
    
    # Monitoring
    config['nitro_sniper_enabled'] = input(f"{prompt_color} > Arm Nitro Sniper? (y/n): {input_color}").lower() == 'y'
    vanities = input(f"{prompt_color} > Enter vanity URLs to track (comma-separated): {input_color}")
    config['vanity_targets'] = [v.strip() for v in vanities.split(',') if v.strip()]

    # Nuking - using more thematic language
    config['nuke_channel_names'] = input(f"{prompt_color} > Nuke channel name template (use '{{i}}'): {input_color}") or "ruined-by-me-{i}"
    config['nuke_role_names'] = input(f"{prompt_color} > Nuke role name template (use '{{i}}'): {input_color}") or "get-rekt-{i}"
    config['nuke_spam_message'] = input(f"{prompt_color} > Nuke spam payload: {input_color}") or "@everyone This server has been compromised."

    # Profile & Status
    config['status_presets'] = ["Hacking The Gibson", "Watching The Matrix", "Playing with fire", "Listening to the void"]
    
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4)
    
    print(f"\n{Fore.MAGENTA}Configuration saved to 'config.json'. System is armed.")
    
    if not os.path.exists('input/tokens.txt'):
        with open('input/tokens.txt', 'w') as f:
            f.write("# Enter your  access tokens here, one per line\n")
        print(f"{Fore.RED}WARNING: 'input/tokens.txt' created but is empty. Please add tokens to proceed.")
    
    time.sleep(3)
    return config

def load_config():
    """Loads the config file or triggers the interactive generator."""
    if not os.path.exists('config.json'):
        return generate_config_interactive()
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"{Fore.RED}FATAL ERROR: 'config.json' is corrupted. Deleting it to regenerate on next start.")
        os.remove('config.json')
        time.sleep(3)
        sys.exit()

# Note on integration:
# To use the new functions, your main.py should call them.
# Example modification in main.py's main() function:
#
# -> print_animated_header(len(tokens))
# -> print_options_menu()
# -> animate_loading("Initializing bot instances")
#
# This comment is for guidance; no changes to main.py are required for this file to work.