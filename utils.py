import json

import disnake
from disnake.ext import commands
from rich.console import Console
from datetime import datetime, timedelta
import re

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