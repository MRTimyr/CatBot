import json

import disnake
from disnake.enums import Locale
from rich.console import Console
from datetime import datetime, timedelta
import re
import os

console = Console()

def _config():
    with open("config.json", "r") as config:
        return json.load(config)

Config = _config()

def ConsoleLog(string: str):
    now = datetime.now()
    return console.print(
        f"[#0000ff][{now.hour}:{now.minute}:{now.second}][/#0000ff][#ff00ff] / [/#ff00ff][#00ff00][INFO][/#00ff00]: {string}"
    )
def ConsoleWarning(string: str):
    now = datetime.now()
    return console.print(
        f"[#0000ff][{now.hour}:{now.minute}:{now.second}][/#0000ff][#ff00ff] / [/#ff00ff][#ff8c00][WARNING][/#ff8c00]: {string}"
    )
def ConsoleError(string: str):
    now = datetime.now()
    return console.print(
        f"[#0000ff][{now.hour}:{now.minute}:{now.second}][/#0000ff][#ff00ff] / [/#ff00ff][#ff0000][ERROR][/#ff0000]: [#ff4500]{string}[/#ff4500]"
    )
def ConsoleText(string: str):
    return console.print(
        f"[gray]* {string}[/gray]"
    )
def ConsoleList(title: str, list: list):
    now = datetime.now()
    List = ""
    for lis in list:
        List += "[#00ff00]•[/#00ff00] " + str(lis) + "\n"
    return console.print(
        f"[#0000ff][{now.hour}:{now.minute}:{now.second}][/#0000ff][#ff00ff] / [/#ff00ff][#00ff00][INFO][/#00ff00]: {title}\n{List}"
    )
def ConsolePanel(title: str, text: list, color: str = "#ffffff", size = 30):
    header = f"[{color}]┌─\[ {title} ]" + "─" * (size - len(title) - 7) + f"┐[/{color}]\n"
    t = ""
    for text in text:
        t += f"[{color}]│ [/{color}]" + text + " " * (size - len(text) - 3) + f"[{color}]│[/{color}]" + "\n"
    futer = f"[{color}]└" + "─" * (size - len(title) + 2) + f"┘[/{color}]"
    console.print(header+t+futer)

def to_date(time: str):
    dtn = datetime.now()
    for string in time.split():
        if re.search(r"[0-9]+s\b", string=string):
            dtn += timedelta(seconds=int(string.replace("s", ""))) #S
        if re.search(r"[0-9]+m\b", string=string):
            dtn += timedelta(minutes=int(string.replace("m", ""))) #M
        if re.search(r"[0-9]+h\b", string=string):
            dtn += timedelta(hours=int(string.replace("h", ""))) #H
        if re.search(r"[0-9]+d\b", string=string):
            dtn += timedelta(days=int(string.replace("d", ""))) #D
    return dtn

def error(inter: disnake.ApplicationCommandInteraction, name: str):
    load = json.load(open("src/error.json", "r", encoding="utf-8"))
    def local():
        if inter.locale == Locale.ru:
            return load[name]["ru"]
        elif inter.locale == Locale.en_US:
            return load[name]["en"]
        elif inter.locale == Locale.en_GB:
            return load[name]["en"]
        elif inter.locale == Locale.uk:
            return load[name]["uk"]
        else:
            return load[name]["en"]

    embed = disnake.Embed(
        color=disnake.Color.red(),
        description=local()
    )
    embed.set_author(
        name="ERROR:"
    )
    return inter.send(embed=embed, ephemeral=True)

class BotColor:
    embed_bg = 0x2F3136

BotColor = BotColor()