# Discord Killer

A customizable self-bot toolkit for advanced Discord users to automate tasks via a stylish command-line interface with logging.  

**⚠️ Warning:** Self-bots violate Discord’s Terms of Service. Use at your own risk — the developers are not responsible for bans or consequences.  

## Features  
- **Custom Prefix** – Change the bot command prefix (default: `.`)  
- **Auto Cog Loading** – Loads Python cog files from the `cogs` folder  
- **Multi-Token Support** – Reads tokens from `input/tokens.txt`  
- **First-Run Config** – Interactive setup wizard  
- **Logging** – Console + file logs with timestamps and colors  
- **Sleek CLI** – Animated header, 2-column menu, and loading animation  


## Prerequisites

- **Python 3.10**: Download and install from [python.org](https://www.python.org/downloads/release/python-310/).
- A valid Discord user token (not a bot token) placed in `input/tokens.txt`.

## Installation

1. Clone or download the repository:
   ```bash
   git clone https://github.com/sinrazed/discordkiller.git
   cd discordkiller
   ```

2. Install dependencies from `requirements.txt` and run :
   ```bash
   pip install -r requirements.txt
   python main.py
   ```

3. **Optional**: If you encounter module errors or issues, create a virtual environment:
   ```bash
   python -m venv myenv
   myenv\Scripts\activate  
   pip install -r requirements.txt
   ```

## Running the Script

1. Ensure you have Python 3.10 installed (**3.10 is MUST**)  
   [Download Python 3.10.6 (64-bit)](https://www.python.org/ftp/python/3.10.6/python-3.10.6-amd64.exe)

2. Run the script:
   ```bash
   python main.py
   ```
3. On first run, the script will prompt you to configure settings interactively.


## Available Command Modules

The CLI menu displays the following modules (functionality depends on cogs in the `cogs` directory):

1. Server nuker
2. Webhook Raid
3. Mass DM Assault
4. VC Connection Flooder
5. Friend Request Spam
6. Profile Cycler
7. Guild Cloner
8. Mass Server Leave
9. Nitro Code Sniper
10. Vanity URL Sniper
11. Username Tracker
12. RPC Controller
13. Token Validator
14. System Purge


## Disclaimer

This tool is for educational purposes only. Using self-bots can result in account termination by Discord. The developers are not liable for any misuse or consequences.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
