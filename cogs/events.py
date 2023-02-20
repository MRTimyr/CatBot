import disnake
from disnake.ext import commands
from utils import ConsoleLog, ConsoleWarning, ConsoleError, ConsoleList, ConsolePanel, error
from bot import cogs

class Events(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_connect(self):
        ConsoleWarning("Starting...")

    @commands.Cog.listener()
    async def on_ready(self):
        ConsoleLog(f"{self.bot.user.name} / {self.bot.status.name}")

    @commands.Cog.listener()
    async def on_slash_command_error(self, inter: disnake.ApplicationCommandInteraction, exception: str):
        if not inter.guild:
            await error(inter, "guild_not_found")
        else:
            ConsoleError(exception)

    @commands.Cog.listener()
    async def on_error(self, event: str):
        ConsoleError(event)

    @commands.Cog.listener()
    async def on_message(self, message: disnake.Message):
        if self.bot.user.mention in message.content:
            await message.add_reaction(
                "🐱"
            )
            ConsoleLog(f"{message.author} mention {self.bot.user}")

def setup(bot: commands.Bot):
    bot.add_cog(Events(bot))