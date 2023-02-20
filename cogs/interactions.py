import disnake
from disnake.ext import commands
import requests
from utils import Config, ConsoleLog, BotColor
import random

class Interactions(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(
        name="kiss",
        description="поцеловать участника",
    )
    async def kiss(self, inter: disnake.ApplicationCommandInteraction, user: disnake.Member):
        site = requests.get(f"https://api.giphy.com/v1/gifs/search?api_key={Config['api_keys']['giphy']}&q=anime+kiss")
        if site.status_code == 200:
            url = site.json()["data"][random.randint(0, len(site.json()["data"]))]
            embed = disnake.Embed(
                description=f"""
                **{inter.author.mention} целует {user.mention}**
                """,
                color=BotColor.embed_bg
            )
            embed.set_image(
                url=url['images']['original']['url']
            )
            await inter.send(embed=embed)

    @commands.user_command(
        name="kiss"
    )
    async def kiss(self, inter: disnake.ApplicationCommandInteraction, user: disnake.Member):
        site = requests.get(f"https://api.giphy.com/v1/gifs/search?api_key={Config['api_keys']['giphy']}&q=anime+kiss")
        if site.status_code == 200:
            url = site.json()["data"][random.randint(0, len(site.json()["data"]))]
            embed = disnake.Embed(
                description=f"""
                    **{inter.author.mention} целует {user.mention}**
                    """,
                color=BotColor.embed_bg
            )
            embed.set_image(
                url=url['images']['original']['url']
            )
            await inter.send(embed=embed)

    @commands.slash_command(
        name="hug",
        description="обнять участника"
    )
    async def hug(self, inter: disnake.ApplicationCommandInteraction, user: disnake.Member):
        site = requests.get(f"https://api.giphy.com/v1/gifs/search?api_key={Config['api_keys']['giphy']}&q=anime+hug")
        if site.status_code == 200:
            url = site.json()["data"][random.randint(0, len(site.json()["data"]))]
            embed = disnake.Embed(
                description=f"""
                **{inter.author.mention} обнимает {user.mention}**
                """,
                color=BotColor.embed_bg
            )
            embed.set_image(
                url=url['images']['original']['url']
            )
            await inter.send(embed=embed)

    @commands.user_command(
        name="hug"
    )
    async def hug(self, inter: disnake.ApplicationCommandInteraction, user: disnake.Member):
        site = requests.get(f"https://api.giphy.com/v1/gifs/search?api_key={Config['api_keys']['giphy']}&q=anime+hug")
        if site.status_code == 200:
            url = site.json()["data"][random.randint(0, len(site.json()["data"]))]
            embed = disnake.Embed(
                description=f"""
                    **{inter.author.mention} обнимает {user.mention}**
                    """,
                color=BotColor.embed_bg
            )
            embed.set_image(
                url=url['images']['original']['url']
            )
            await inter.send(embed=embed)

    @commands.slash_command(
        name="pat",
        description="погладить участника"
    )
    async def pat(self, inter: disnake.ApplicationCommandInteraction, user: disnake.Member):
        site = requests.get(f"https://api.giphy.com/v1/gifs/search?api_key={Config['api_keys']['giphy']}&q=anime+pat")
        if site.status_code == 200:
            url = site.json()["data"][random.randint(0, len(site.json()["data"]))]
            embed = disnake.Embed(
                description=f"""
                **{inter.author.mention} гладит {user.mention}**
                """,
                color=BotColor.embed_bg
            )
            embed.set_image(
                url=url['images']['original']['url']
            )
            await inter.send(embed=embed)

    @commands.user_command(
        name="pat"
    )
    async def pat(self, inter: disnake.ApplicationCommandInteraction, user: disnake.Member):
        site = requests.get(f"https://api.giphy.com/v1/gifs/search?api_key={Config['api_keys']['giphy']}&q=anime+pat")
        if site.status_code == 200:
            url = site.json()["data"][random.randint(0, len(site.json()["data"]))]
            embed = disnake.Embed(
                description=f"""
                    **{inter.author.mention} гладит {user.mention}**
                    """,
                color=BotColor.embed_bg
            )
            embed.set_image(
                url=url['images']['original']['url']
            )
            await inter.send(embed=embed)
def setup(bot: commands.Bot):
    bot.add_cog(Interactions(bot))