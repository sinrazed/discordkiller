import discord
from discord.ext import commands
import asyncio

class Spam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = bot.logger

    @commands.command(name='massdm', help='12. Simulates mass DMing all members in the server.')
    async def massdm(self, ctx, *, message: str):
        self.logger.warning(f"Initiating  MassDM in '{ctx.guild.name}'.")
        dm_count = 0
        for member in ctx.guild.members:
            if not member.bot and member.id != self.bot.user.id:
                try:
                    # await member.send(message)
                    self.logger.info(f"  > (SIM) Sent DM to {member.name}#{member.discriminator}")
                    dm_count += 1
                    await asyncio.sleep(1) # Simulate delay to avoid rate limits
                except Exception:
                    self.logger.warning(f"  > (SIM) Failed to DM {member.name} (closed DMs  ).")
        self.logger.success(f" : MassDM complete. Sent to {dm_count} members.")
        await ctx.send(f" : Attempted to DM {dm_count} members.")

async def setup(bot):
    await bot.add_cog(Spam(bot))