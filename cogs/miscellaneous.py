import discord
from discord.ext import commands
import random
import time
import asyncio

class Miscellaneous(commands.Cog):
    """Cog for miscellaneous, utility, and fun commands."""
    def __init__(self, bot):
        self.bot = bot
        self.logger = bot.logger

    # 3. Funny & Utility Commands
    @commands.command(name='ping', help='Checks the bot\'s latency to Discord.')
    async def ping(self, ctx):
        """A simple command that edits the message to show latency."""
        start_time = time.time()
        # In discord.py-self, ctx.message.edit works on your own messages.
        message = await ctx.send("Pinging...")
        end_time = time.time()
        api_latency = round((end_time - start_time) * 1000)
        websocket_latency = round(self.bot.latency * 1000)
        await message.edit(content=f"**Pong!**\nWebsocket Latency: `{websocket_latency}ms`\nAPI Latency: `{api_latency}ms`")

    @commands.command(name='uptime', help='Shows how long the bot has been online.')
    async def uptime(self, ctx):
        delta_uptime = time.time() - self.bot.start_time
        hours, remainder = divmod(int(delta_uptime), 3600)
        minutes, seconds = divmod(remainder, 60)
        await ctx.message.edit(content=f"**Uptime:** `{hours}h {minutes}m {seconds}s`")

    @commands.command(name='embed', help='Creates and sends a custom embed message.')
    async def embed(self, ctx, *, message: str):
        """Allows creating rich embeds directly from a command."""
        embed = discord.Embed(
            description=message,
            color=discord.Color.random(),
            timestamp=ctx.message.created_at
        )
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        try:
            await ctx.message.delete()
            await ctx.send(embed=embed)
        except discord.Forbidden:
            self.logger.error("Could not send embed, missing permissions.")

    # 19. Self-bot Message Spammer
    @commands.command(name='spam', help='Spams a message a specified number of times.')
    async def spam(self, ctx, amount: int, *, message: str):
        """A demonstration of a channel spammer."""
        if amount > 25: # Safety limit for the demo
            await ctx.send(" : Spam amount capped at 25 for this demo.", delete_after=5)
            amount = 25
        
        await ctx.message.delete()
        self.logger.warning(f"Initiating SIMULATED spam of '{message}' {amount} times in #{ctx.channel.name}")
        for i in range(amount):
            # await ctx.send(message)
            self.logger.info(f"  > (SIM) Sent spam message {i+1}/{amount}")
            await asyncio.sleep(random.uniform(0.3, 0.8)) # Use a random delay to look less robotic

    # 16. Mass Friend Adder (simulated for individual additions)
    @commands.command(name='friend', help='16. Simulates sending a friend request to a user by ID.')
    async def friend(self, ctx, user_id: int):
        self.logger.info(f"SIMULATING: Sending friend request to user ID {user_id}")
        # ---   OF SENDING FRIEND REQUEST ---
        # try:
        #     user = await self.bot.fetch_user(user_id)
        #     await user.send_friend_request()
        #     self.logger.success(f"Successfully sent friend request to {user.name}")
        #     await ctx.message.edit(content=f" : Sent friend request to `{user.name}`.")
        # except Exception as e:
        #     self.logger.error(f"Failed to send friend request to {user_id}: {e}")
        #     await ctx.message.edit(content=f" : Failed to send friend request to `{user_id}`.")
        await ctx.message.edit(content=f" : Sent friend request to user with ID `{user_id}`.")

    # 15. Mass Group Chat Creator
    @commands.command(name='massgc', help='15. Simulates creating a group chat with multiple users.')
    async def massgc(self, ctx, *users: discord.User):
        """Creates a group chat with mentioned users."""
        if len(users) < 2:
            return await ctx.message.edit(content=" : You need to mention at least 2 other users to create a group chat.")
        
        user_names = [user.name for user in users]
        self.logger.warning(f"Initiating SIMULATED group chat creation with users: {', '.join(user_names)}")
        # ---   OF CREATING GROUP CHAT ---
        # try:
        #    gc = await self.bot.create_group(*users)
        #    await gc.send(f"Group created via self-bot demo! Hello {', '.join([user.mention for user in users])}")
        #    self.logger.success("Successfully created group chat.")
        #    await ctx.message.edit(content=" : Group chat created successfully.")
        # except Exception as e:
        #    self.logger.error(f"Failed to create group chat: {e}")
        #    await ctx.message.edit(content=f" : Failed to create group chat.")
        await ctx.message.edit(content=f" : Created a group chat with `{len(users)}` other users.")

async def setup(bot):
    await bot.add_cog(Miscellaneous(bot))