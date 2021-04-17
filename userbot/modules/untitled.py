from asyncio import create_subprocess_exec as asyncrunapp

from asyncio.subprocess import PIPE as asyncPIPE

from os import remove
from platform import python_version, uname
from shutil import which
from telethon import version

from userbot import ALIVE_LOGO, ALIVE_NAME, CMD_HELP, LBOT_VERSION, bot
from userbot.events import register

# ================= CONSTANT ===================
DEFAULTUSER = ALIVE_NAME or "Defina a ConfigVar 'ALIVE_NAME' !"
# ===================================≠=≠========

@register(outgoing=True, pattern=r"^.(of|af)$")
async def amireallyalive(alive):
  """ Para o comando .alive, verifique se o bot está rodando. """
  output = (
    f""" **LzinBot funcionando perfeitamente**
  • python: v{python_version()}
  • user: {DEFAULTUSER}
"""
  )
  else:
    await alive.edit(output)