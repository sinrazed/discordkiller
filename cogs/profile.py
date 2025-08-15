import discord
from discord.ext import commands, tasks
import random
from pypresence import Presence # For RPC  

class Profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = bot.logger
        self.status_changer.start()
        self.rpc_active = False
        self.rpc_client_id = "123456789012345678" # Dummy Client ID for RPC

    @tasks.loop(seconds=600)
    async def status_changer(self):
        # 7. Auto status changer
        new_status = random.choice(self.bot.config.get('status_presets', []))
        self.logger.info(f"SIMULATING: Auto-changing status to: Playing '{new_status}'")
        # await self.bot.change_presence(activity=discord.Game(name=new_status))

    @commands.command(name='bio', help='8. Simulates changing your bio/about me.')
    async def bio(self, ctx, *, new_bio: str):
        self.logger.info(f"SIMULATING: Changing bio to '{new_bio[:50]}...'")
        # profile = await self.bot.fetch_user_profile(self.bot.user.id)
        # await profile.edit(bio=new_bio)
        await ctx.send(f" : Bio has been set to: `{new_bio}`")
        
    @commands.command(name='rpc', help='6. Toggles a simulated Rich Presence.')
    async def rpc(self, ctx):
        if self.rpc_active:
            self.logger.info("SIMULATING: Stopping Rich Presence.")
            # self.RPC.close()
            self.rpc_active = False
            await ctx.send(" : RPC Disabled.")
        else:
            self.logger.info("SIMULATING: Starting Rich Presence.")
            try:
                # self.RPC = Presence(self.rpc_client_id)
                # self.RPC.connect()
                # self.RPC.update(state="Hacking the Gibson", details="Self-Bot Demo Suite", large_image="hacker", small_image="python", start=int(time.time()))
                self.rpc_active = True
                await ctx.send(" : RPC Enabled.")
            except Exception as e:
                self.logger.error(f" : RPC failed to start. {e}")

async def setup(bot):
    await bot.add_cog(Profile(bot))