# Don't remove This Line From Here.
# Telegram :- @ll_ALPHA_BABY_lll

import random
from datetime import datetime

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from config import IMG, OWNER_USERNAME, STICKER
from RAUSHAN import BOT_NAME, dev
from RAUSHAN.database.chats import add_served_chat
from RAUSHAN.database.users import add_served_user
from RAUSHAN.modules.helpers import PNG_BTN


@dev.on_message(filters.command("ping", prefixes=["+", "/", "-", "?", "$", "&"]))
async def ping(_, message: Message):
    await message.reply_sticker(sticker=random.choice(STICKER))
    start = datetime.now()
    loda = await message.reply_photo(
        photo=random.choice(IMG),
        caption="ᴘɪɴɢ ᴘᴏɴɢ...",
    )
    try:
        await message.delete()
    except:
        pass

    ms = (datetime.now() - start).microseconds / 1000
    await loda.edit_text(
        text=f"нєყ вαву!!\n{BOT_NAME} 𝚒ѕ al𝚒ve 🥀 αnd worĸɪng ғɪnє wɪтн ᴀ ᴘɪɴɢ oғ\n➥ `{ms}` ms\n\n<b> мα𝙳є ω𝚒тн ❣️ ву [𝗟𝗘𝗚𝗘𝗡𝗗 𝗠𝗜𝗖𝗞𝗘𝗬](https://t.me/{OWNER_USERNAME}) </b>",
        reply_markup=InlineKeyboardMarkup(PNG_BTN),
    )
    if message.chat.type == ChatType.PRIVATE:
        await add_served_user(message.from_user.id)
    else:
        await add_served_chat(message.chat.id)
