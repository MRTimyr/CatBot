import disnake
from disnake.ext import commands
import json

import utils
from utils import error

class Control(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(
        name="control",
        guild_ids=[1010140326758981692, 1029318503330742272]
    )
    async def control(self, inter: disnake.ApplicationCommandInteraction): ...

    async def help_autocomplete(inter: disnake.ApplicationCommandInteraction, string: str) -> list[str]:
        load = json.load(open("./src/error.json"))
        command_list = []
        for key, value in load.items():
            command_list.append(key)
        string = string.lower()
        return [lang for lang in command_list if string in lang.lower()]

    @control.sub_command(name="error")
    async def error(
            self,
            inter: disnake.ApplicationCommandInteraction,
            error: str = commands.Param(
                name="error-name",
                autocomplete=help_autocomplete
            )
    ):
        await utils.error(inter, error)

def setup(bot: commands.Bot):
    bot.add_cog(Control(bot))