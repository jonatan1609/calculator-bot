from pyrogram import Client, types
from .utils import Keyboards


@Client.on_message()
async def new_message_handler(_client: Client, message: types.Message):
    await message.reply("Calculate here:\n‎", reply_markup=Keyboards.calculator.value)

