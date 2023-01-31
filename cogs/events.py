import disnake
from disnake.ext import commands
from utils import ConsoleLog, ConsoleWarning, ConsoleError, ConsoleList, ConsolePanel
from bot import cogs

class Events(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        ConsoleLog(f"run!")
        ConsoleList (
            title=f"{self.bot.user.name}:",
            list=[
                f"Users: {len(self.bot.users)}",
                f"Guilds: {len(self.bot.guilds)}"
            ]
        )
        ConsolePanel (
            title="cogs",
            text=cogs,
            color="#00ff00"
        )

    @commands.Cog.listener()
    async def on_slash_command_error(self, inter: disnake.AppCommandInteraction, exception: str):
        if not inter.guild:
            await inter.send(
                embed=disnake.Embed(
                    description=f"`для работы данной команды необходим сервер!`",
                    color=disnake.Color.red()
                )\
                .set_author(name="ERROR.Guild.not_found:"),
                ephemeral=True
            )
        else:
            ConsoleError(exception)

def setup(bot: commands.Bot):
    bot.add_cog(Events(bot))