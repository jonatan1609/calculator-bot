from pyrogram import Client, types
from .utils import Filters, Messages


@Client.on_message(Filters.START.value)
async def start_handler(_client: Client, message: types.Message):
    await message.reply(Messages.START.value)
