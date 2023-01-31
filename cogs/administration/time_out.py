import disnake
from disnake.ext import commands
from disnake import utils
from utils import to_date

class Time_Out(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="time-out")
    async def time_out(self, inter: disnake.ApplicationCommandInteraction): ...

    @time_out.sub_command(
        name="add"
    )
    async def time_out_add(
            self,
            inter: disnake.ApplicationCommandInteraction,
            member: disnake.Member,
            time: str,
            reasons: str = "[ не указана ]"
    ):
        if inter.user.guild_permissions.moderate_members == True:
            timeout = await member.timeout(
                until=to_date(time),
                reason=reasons
            )
            await member.send(
                embed=disnake.Embed(
                    title=f"<:time_out:1068524781282017331> вам выдали time-out на сервере: {inter.guild.name}",
                    color=disnake.Color.red()
                ).add_field(
                    name="время",
                    value=f"{utils.format_dt(timeout.created_at, 'T')}"
                ).add_field(
                    name="администратор",
                    value=inter.author.mention
                ).add_field(
                    name="причина",
                    value=f"```{reasons}```",
                    inline=False
                ).set_thumbnail(
                    file=disnake.File("src/time-out.png", filename="time-out.png")
                )
            )
            await inter.send(
                embed=disnake.Embed(
                    title=f"<:time_out:1068524781282017331> участнику: {member.name} был выдан time-out",
                    color=disnake.Color.green()
                ).add_field(
                    name="время",
                    value=f"{utils.format_dt(timeout.created_at, 'T')}"
                ).add_field(
                    name="администратор",
                    value=inter.author.mention
                ).add_field(
                    name="причина",
                    value=f"```{reasons}```",
                    inline=False
                ).set_thumbnail(
                    file=disnake.File("src/time-out.png", filename="time-out.png")
                )
            )

    @time_out.sub_command(
        name="remove"
    )
    async def time_out_remove(
            self,
            inter: disnake.ApplicationCommandInteraction,
            member: disnake.Member
    ):
        if inter.user.guild_permissions.moderate_members == True:
            if not member.current_timeout:
                timeout = await member.timeout(
                    until=None,
                    reason=None
                )
                member_embed = disnake.Embed(
                    title=f"с вас сняли time-out "
                )
                await member.send(
                    embed=member_embed
                )


def setup(bot: commands.Bot):
    bot.add_cog(Time_Out(bot))