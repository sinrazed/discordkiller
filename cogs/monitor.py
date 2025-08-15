import discord
from discord.ext import commands, tasks
import asyncio
import random
import re
import time

class Monitoring(commands.Cog):
    """Cog for background monitoring tasks."""
    def __init__(self, bot):
        self.bot = bot
        self.logger = bot.logger
        self.claimed_nitros = set()
        self.target_username = None  # Set by the 'trackuser' command

        # Start background tasks if they are configured
        if self.bot.config.get('nitro_sniper_enabled', False):
            self.logger.info("Nitro Sniper is enabled and listening.")
        
        if self.bot.config.get('vanity_targets'):
            self.vanity_tracker.start()
        
    def cog_unload(self):
        """Cleanly stops tasks when the cog is unloaded."""
        self.vanity_tracker.cancel()
        if self.username_monitor.is_running():
            self.username_monitor.cancel()

    # 18. Nitro Sniper
    @commands.Cog.listener()
    async def on_message(self, message):
        """Listens for messages to find and 'claim' Nitro gifts."""
        if not self.bot.config.get('nitro_sniper_enabled', False):
            return
        
        # Regex to find different forms of gift links
        gift_regex = r'(discord\.gift/|discordapp\.com/gifts/|discord\.com/gifts/)([a-zA-Z0-9]{16,24})'
        match = re.search(gift_regex, message.content)
        
        if match:
            code = match.group(2)
            if code in self.claimed_nitros:
                return  # Avoid re-processing the same code
            
            self.logger.warning(f"Nitro link detected in '{message.guild.name}' -> #{message.channel.name}!")
            self.claimed_nitros.add(code)
    
            
            claim_time = random.uniform(0.05, 0.25) # Simulate network latency and processing time
            await asyncio.sleep(claim_time)
            
            # Simulate a realistic outcome
            if random.random() < 0.75:  # 75% chance it's fake, already claimed, or we were too slow
                self.logger.error(f"  > (SIM) Failed to claim Nitro code '{code}'. (Already claimed/Invalid)")
            else:
                self.logger.success(f"  > (SIM) SUCCESSFULLY SNIPED NITRO CODE: '{code}' in {claim_time:.3f}s!")

    # 17. Vanity Tracker
    @tasks.loop(minutes=5.0)
    async def vanity_tracker(self):
        targets = self.bot.config.get('vanity_targets', [])
        if not targets:
            self.vanity_tracker.cancel()
            return
            
        self.logger.info("Vanity Tracker: Performing periodic check on configured vanities.")
        for vanity_url in list(targets): # Iterate over a copy to allow modification
            vanity_code = vanity_url.split('/')[-1]
            self.logger.info(f"  > (SIM) Checking availability for vanity: discord.gg/{vanity_code}")
            
            # Simulate a 1% chance the vanity has become available
            if random.random() < 0.01:
                self.logger.success(f"  > (SIM) VANITY '{vanity_code}' APPEARS TO BE AVAILABLE! ATTEMPTING TO CLAIM...")
                self.logger.success(f"  > (SIM) PATCH request to claim 'discord.gg/{vanity_code}' has been sent!")
                self.bot.config['vanity_targets'].remove(vanity_url)

            await asyncio.sleep(3) # Stagger checks to look more natural

    @vanity_tracker.before_loop
    async def before_vanity_tracker(self):
        await self.bot.wait_until_ready()

    # 4. Username Checker and Monitor
    @commands.command(name='trackuser', help='4. Monitors for a username to become available.')
    async def track_user(self, ctx, username: str):
        if self.username_monitor.is_running():
            self.username_monitor.cancel()
            self.target_username = None
            await ctx.message.edit(content=" : Username tracking has been stopped.")
        else:
            self.target_username = username
            if not self.username_monitor.is_running():
                self.username_monitor.start()
            await ctx.message.edit(content=f" : Now monitoring for username `{username}`. I will check every 30 minutes.")

    @tasks.loop(minutes=30.0)
    async def username_monitor(self):
        if not self.target_username:
            self.username_monitor.cancel()
            return

        self.logger.info(f"Username Monitor: Checking availability for '{self.target_username}'...")
        # Simulate a 5% chance of being available on each check
        if random.random() < 0.05:
            self.logger.success(f"  > (SIM) USERNAME '{self.target_username}' IS AVAILABLE!")
            # ---   OF CHANGING USERNAME ---
            # await self.bot.user.edit(username=self.target_username)
            self.logger.success(f"  > (SIM) ATTEMPTING TO CHANGE USERNAME to '{self.target_username}'!")
            await self.bot.get_user(self.bot.user.id).send(f" : The username `{self.target_username}` is now available! I have attempted to claim it.")
            self.username_monitor.cancel()
        else:
            self.logger.info(f"  > (SIM) Username '{self.target_username}' is still taken.")

async def setup(bot):
    await bot.add_cog(Monitoring(bot))