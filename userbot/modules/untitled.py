from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot
from userbot.events import register
from userbot.utils import time_formatter

   @register(outgoing=True, pattern=r"^\.fnix$")
   async def fnix(e):
     await e.edit(
       "**tu é um corno fnix** \n"
       )


@register(outgoing=True, pattern=r"^\.samu$")
async def samu(e):
  await e.edir(
    "samuel é ruim, ruim em python, mds"
    )
