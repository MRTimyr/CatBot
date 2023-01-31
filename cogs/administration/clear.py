import disnake
from disnake.ext import commands
import asyncio

class Clear(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(
        name="clear"
    )
    async def test(
            self,
            inter: disnake.ApplicationCommandInteraction,
            messages: int = commands.Param(
                lt=100,
                gt=1
            )
    ):
        await inter.response.defer()
        messag = await inter.channel.purge(limit=messages)
        embed = disnake.Embed(
            title="сообщения очищены",
            description=f"""
            **Очищенно:** {len(messag)}
            """,
            color=disnake.Color.blurple()
        )
        await inter.channel.send(
            embed = embed
        )


def setup(bot: commands.Bot):
    bot.add_cog(Clear(bot))