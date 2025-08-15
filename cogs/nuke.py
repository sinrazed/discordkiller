import discord
from discord.ext import commands
import asyncio
import random

class Nuking(commands.Cog):
    """Cog for all server destruction  s."""
    def __init__(self, bot):
        self.bot = bot
        self.logger = bot.logger

    @commands.command(name='nuke', help='1. Simulates a full server nuke.')
    async def nuke(self, ctx):
        if not ctx.guild:
            return await ctx.send(" : This command can only be used in a server.")
        
        self.logger.warning(f"Initiating SIMULATED nuke on server: {ctx.guild.name} ({ctx.guild.id})")
        
        # Phase 1: Rename Server
        new_name = f"NUKED BY {self.bot.user.name}"
        self.logger.info(f"SIMULATING: Renaming server to '{new_name}'")
        # await ctx.guild.edit(name=new_name, reason="Nuke  ")

        # Phase 2: Mass Channel & Role Creation (Concurrent)
        self.logger.info("SIMULATING: Mass channel and role creation.")
        channel_tasks = [
            self.simulate_create_channel(ctx.guild, self.bot.config['nuke_channel_names'].format(i=i))
            for i in range(25)
        ]
        role_tasks = [
            self.simulate_create_role(ctx.guild, self.bot.config['nuke_role_names'].format(i=i))
            for i in range(25)
        ]
        await asyncio.gather(*channel_tasks, *role_tasks)

        # Phase 3: Mass Webhook Creation and Spam
        self.logger.info("SIMULATING: Mass webhook creation and spam in all text channels.")
        webhook_spam_tasks = [
            self.simulate_webhook_spam(channel) for channel in ctx.guild.text_channels
        ]
        await asyncio.gather(*webhook_spam_tasks)

        self.logger.success(f"SIMULATED nuke on {ctx.guild.name} complete.")

    async def simulate_create_channel(self, guild, name):
        # await guild.create_text_channel(name)
        self.logger.info(f"  > (SIM) Created text channel: #{name}")
        await asyncio.sleep(0.1)

    async def simulate_create_role(self, guild, name):
        # await guild.create_role(name=name, color=discord.Color.random())
        self.logger.info(f"  > (SIM) Created role: @{name}")
        await asyncio.sleep(0.1)

    async def simulate_webhook_spam(self, channel):
        try:
            # webhook = await channel.create_webhook(name="Nuke Spammer")
            self.logger.info(f"  > (SIM) Created webhook in #{channel.name}")
            for _ in range(10):
                # await webhook.send(self.bot.config['nuke_spam_message'], username=f"Nuked by {self.bot.user.name}")
                self.logger.info(f"    - (SIM) Webhook sent message to #{channel.name}")
                await asyncio.sleep(0.05)
        except Exception as e:
            self.logger.warning(f"  > (SIM) Could not create/spam webhook in #{channel.name} (permission  ).")

    @commands.command(name='massleave', help='9. Simulates leaving all servers except the current one.')
    async def massleave(self, ctx):
        self.logger.warning("Initiating SIMULATED mass server leave.")
        count = 0
        for guild in self.bot.guilds:
            if guild.id != ctx.guild.id:
                # await guild.leave()
                self.logger.info(f"SIMULATING: Left server '{guild.name}' ({guild.id})")
                count += 1
                await asyncio.sleep(0.5)
        self.logger.success(f" : Left {count} servers.")
        await ctx.send(f" : Process to leave {count} servers complete.")

    @commands.command(name='masscreate', help='10. Simulates creating multiple servers.')
    async def masscreate(self, ctx, amount: int = 5):
        self.logger.warning(f"Initiating SIMULATED mass server creation of {amount} servers.")
        for i in range(amount):
            server_name = f"{self.bot.user.name}'s Server {random.randint(100,999)}"
            # await self.bot.create_guild(name=server_name)
            self.logger.info(f"SIMULATING: Created server '{server_name}'")
            await asyncio.sleep(1)
        self.logger.success(f" : Created {amount} servers.")
        await ctx.send(f" : Process to create {amount} servers complete.")


async def setup(bot):
    await bot.add_cog(Nuking(bot))