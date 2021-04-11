# pylint: disable=invalid-name, missing-module-docstring
#
#
# This file is part of < https://github.com/samuca78/LzinhoBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/samuca78/LzinhoBot/blob/master/LICENSE >
#
# All rights reserved.

import os
import asyncio

from pyrogram import Client
from dotenv import load_dotenv

if os.path.isfile("config.env"):
    load_dotenv("config.env")


async def genStrSession() -> None:  # pylint: disable=missing-function-docstring
    async with Client(
            "LzinhoBot",
            api_id=int(os.environ.get("API_ID") or input("Enter Telegram APP ID: ")),
            api_hash=os.environ.get("API_HASH") or input("Enter Telegram API HASH: ")
    ) as userge:
        print("\nprocessing...")
        await lzinhobot.send_message(
            "me", f"#LZINHOBOT #STRING_SESSION\n\n```{await lzinhobot.export_session_string()}```")
        print("Pronto! Sua String Session foi enviada para as mensagens salvas!")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(genStrSession())
