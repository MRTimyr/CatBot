import disnake
from disnake.ext import commands
from utils import Config
from typing import Union

class Info(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # info
    @commands.slash_command(
        name="info"
    )
    async def info(self, inter: disnake.AppCommandInteraction):
        return None


#info user
    @info.sub_command(
        name="user",
        description=disnake.Localised(
            data={
                disnake.Locale.ru: "выводит информацию о пользователе",
                disnake.Locale.en_US: "shows information about the user",
                disnake.Locale.en_GB: "shows information about the user",
                disnake.Locale.uk: "виводить інформацію про Користувача"
            }
        )
    )
    async def info_user (
            self,
            inter: disnake.AppCommandInteraction,
            user: disnake.Member = commands.Param(
                default=None
            )
    ):
        if user == None:
            user = inter.user
        else:
            user = user

        def _name():
            if user.display_name != user.name:
                return f"`{user.display_name}` (`{user.name}#{user.tag}`)"
            if user.display_name == user.name:
                return f"`{user.name}#{user.tag}`"
        def _avatar():
            if user.avatar != None:
                return user.avatar.url
            if user.avatar == None:
                return None
        def _avatar_guild():
            if user.guild_avatar != None:
                return user.guild_avatar.url
            if user.guild_avatar == None:
                return user.avatar.url
        def _color():
            if str(user.top_role.color) == "#000000":
                return disnake.Color.blurple()
            else:
                return user.top_role.color
        def _roles():
            r = ""
            for role in user.roles:
                r += str(role.mention) + ", "
            return r[:-2]

        embed = disnake.Embed(
            title=f"информация о пользователе: {user.name}",
            color=_color(),
            description=f"""
            **Имя:** {_name()}
            **Статус:** `{user.status.name}`
            **Создан:** {disnake.utils.format_dt(user.created_at, "f")} ({disnake.utils.format_dt(user.created_at, "R")})
            **На сервере:** {disnake.utils.format_dt(user.joined_at, "f")} ({disnake.utils.format_dt(user.joined_at, "R")})
            **ID:** `{user.id}`
            """
        )
        embed.set_thumbnail(
            url=_avatar_guild()
        )
        embed.set_author(
            icon_url=_avatar(),
            name=f"иформация о {user.display_name}"
        )
        embed.add_field(
            name="роли",
            value=_roles()
        )


        await inter.response.send_message(
            embed=embed
        )


#info guild
    @info.sub_command(
        name="guild",
        description=disnake.Localised(
            data={
                disnake.Locale.ru: "выводит информацию о сервере",
                disnake.Locale.en_US: "shows information about the guild",
                disnake.Locale.en_GB: "shows information about the guild",
                disnake.Locale.uk: "виводить інформацію про сервер"
            }
        )
    )
    async def info_guild(
            self,
            inter: disnake.AppCommandInteraction
    ):
        guild = inter.guild
        def _members_online():
            online = 0
            for member in guild.members:
                if member.status == disnake.Status.online:
                    online += 1
                if member.status == disnake.Status.dnd:
                    online += 1
                if member.status == disnake.Status.idle:
                    online += 1
            return online
        def _members_offline():
            offline = 0
            for member in guild.members:
                if member.status == disnake.Status.offline:
                    offline += 1
            return offline
        def _bots():
            bots = 0
            for bot in guild.members:
                if bot.bot:
                    bots += 1
            return bots

        def _icon():
            icon = None
            if guild.icon != None:
                icon = guild.icon.url
            return icon
        def _baner():
            baner = None
            if guild.banner != None:
                baner = guild.banner.url
            return baner

        def _roles_administrator():
            admin = 0
            for roles in guild.roles:
                if roles.permissions.administrator == True:
                    admin += 1
            return admin

        def _premium_subscription_lvl():
            if guild.premium_subscription_count == 0:
                return "`[0/3]`"
            elif guild.premium_subscription_count >= 2:
                return "`[1/3]`"
            elif guild.premium_subscription_count >= 7:
                return "`[2/3]`"
            elif guild.premium_subscription_count >= 14:
                return "**`[3/3]`**"
            else:
                return f"**`[{guild.mfa_level}/3]`**"

        def _description():
            if guild.description == None:
                return "`[ отсутсвует ]`"
            else:
                return f"```\n{guild.description}\n```"

        embed = disnake.Embed(
            title=f"информация о сервере: {guild.name}",
            color=disnake.Color.blurple(),
            description=f"""
            **Имя:** `{guild.name}`
            **Создатель:** {guild.owner.mention} (`{guild.owner.name}#{guild.owner.tag}`)
            **Дата создания:** {disnake.utils.format_dt(guild.created_at, "f")} ({disnake.utils.format_dt(guild.created_at, "R")})
            **Эмодзи:** `{len(guild.emojis)}`
            **Стикеров:** `{len(guild.stickers)}`
            **LVL буста:** {_premium_subscription_lvl()}
            **ID:** `{guild.id}`
            """
        )
        embed.add_field(
            name="__Описание__",
            value=_description(),
            inline=False
        )
        embed.add_field(
            name="__Участники__",
            value=f"""
            **Всего:** `{len(guild.members)}`
            **Ботов:** `{_bots()}`
            **Онлайн:** `{_members_online()}`
            **Офлайн:** `{_members_offline()}`
            """,
            inline=True
        )
        embed.add_field(
            name="__Каналы__",
            value=f"""
            **Всего:** `{len(guild.channels)}`
            **Текстовые:** `{len(guild.text_channels)}`
            **Голосовые:** `{len(guild.voice_channels)}`
            **Форумы:** `{len(guild.forum_channels)}`
            **Трибун:** `{len(guild.stage_channels)}`
            """,
            inline=True
        )
        embed.add_field(
            name="__Роли__",
            value=f"""
            **Всего:** `{len(guild.roles)}`
            **Администраторов:** `{_roles_administrator()}`
            """,
            inline=True
        )
        embed.set_thumbnail(url=_icon())
        embed.set_image(url=_baner())
        await inter.send(
            embed=embed
        )

#info bot
    @info.sub_command(
        name="bot",
        description=disnake.Localised(
            data={
                disnake.Locale.ru: "выводит информацию о боте",
                disnake.Locale.en_US: "shows information about the bot",
                disnake.Locale.en_GB: "shows information about the bot",
                disnake.Locale.uk: "виводить інформацію про боте"
            }
        )
    )
    async def info_bot(
            self,
            inter: disnake.AppCommandInteraction
    ):
        bot = inter.bot
        def _name():
            if bot.user.display_name != bot.user.name:
                return f"`{bot.user.display_name}` (`{bot.user.name}`)"
            if bot.user.display_name == bot.user.name:
                return f"`{bot.user.name}`"
        embed = disnake.Embed(
            description=f"""
            **Имя:** {_name()}
            """,
            color=disnake.Color.blurple()
        )
        embed.add_field(
            name=f"Версия",
            value=f"`{Config['version']}`"
        )
        embed.add_field(
            name="Автор",
            value=f"`{inter.bot.get_user(Config['creators'])}`"
        )
        embed.add_field(
            name="Пинг",
            value=f"`{round(inter.bot.latency / 60)} ms`"
        )
        embed.add_field(
            name="Ссылки",
            value="[Discord server](https://discord.gg/GaabpYavt2)",
            inline=False
        )
        embed.set_author(
            name=f"информация о боте: {bot.user.name}"
        )
        embed.set_thumbnail(
            url=bot.user.avatar.url
        )
        await inter.send(
            embed=embed
        )

def setup(bot: commands.Bot):
    bot.add_cog(Info(bot))