import disnake
from disnake.ext import commands
from utils import Config

bot = commands.Bot(
    command_prefix="!",
    intents=disnake.Intents.all(),
    help_command=None,
    reload=True
)

cogs = [
    "events",
    "info",
    "help",
    "control",
    "interactions"
]

for cog in cogs:
    bot.load_extension(f"cogs.{cog}")

if __name__ == "__main__":
    bot.run(
        Config["token"]
    )