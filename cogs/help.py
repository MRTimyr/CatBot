import json
from disnake.enums import Locale
import disnake
from disnake.ext import commands
from disnake.enums import Locale
from utils import BotColor, error
from disnake import ButtonStyle

class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    async def help_autocomplete(inter: disnake.ApplicationCommandInteraction, string: str) -> list[str]:
        load = json.load(open("./src/help.json"))
        command_list = []
        for key, value in load['commands'].items():
            command_list.append(key)
        string = string.lower()
        return [lang for lang in command_list if string in lang.lower()]


    @commands.slash_command(
        name="help",
        description=disnake.Localised(
            data={
                disnake.Locale.ru: "выводит информацию о командах",
                disnake.Locale.en_GB: "shows information about commands",
                disnake.Locale.en_US: "shows information about commands",
                disnake.Locale.uk: "виводить інформацію про команди"
            }
        )
    )
    async def help(
            self,
            inter: disnake.ApplicationCommandInteraction,
            command: str = commands.Param(
                autocomplete=help_autocomplete,
                description=disnake.Localised(
                    data={
                        disnake.Locale.ru: "команды бота",
                        disnake.Locale.en_GB: "bot commands",
                        disnake.Locale.en_US: "bot commands",
                        disnake.Locale.uk: "команди бота"
                    }
                )
            )
    ):
        file = json.load(open("./src/help.json", "r", encoding="utf-8"))
        try:
            file['commands'][command]
        except KeyError:
            await error(inter, "help_command_not_found")
        else:
            def local():
                if inter.locale == Locale.ru:
                    return "ru"
                elif inter.locale == Locale.en_US:
                    return "en"
                elif inter.locale == Locale.en_GB:
                    return "en"
                elif inter.locale == Locale.uk:
                    return "uk"
                else:
                    return "en"

            def arguments():
                try:
                    file['commands'][command]['usage']['arguments']
                except KeyError:
                    return ""
                else:
                    argument = ""
                    for arg in file['commands'][command]['usage']['arguments']:
                        argument = "> **•** " + arg + "\n"
                    return argument


            embed = disnake.Embed(
                title=f"Информация о команде: `/{file['commands'][command]['name']}`",
                description=f"{file['commands'][command]['description'][local()]}\n\n**Использование:** `{file['commands'][command]['usage']['name']}`\n{arguments()}",
                color=disnake.Color.blurple()
            )
            await inter.send(
                embed=embed
            )

def setup(bot: commands.Bot):
    bot.add_cog(Help(bot))