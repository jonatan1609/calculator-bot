from pyrogram import Client, types
from .utils import Filters, Messages


@Client.on_message(Filters.START.value, group=-1)
async def start_handler(_client: Client, message: types.Message):
    await message.reply(Messages.START.value.format(name=message.from_user.first_name))
