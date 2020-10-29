from pyrogram import Client, types
from .utils import Keyboards


@Client.on_callback_query()
async def callback_receiver(_client: Client, callback: types.CallbackQuery):
    if callback.data == "C":
        await callback.message.edit(callback.message.text[:-1], reply_markup=Keyboards.calculator.value)
    elif callback.data == "=":
        try:
            res = str(eval(callback.message.text[17:]))
        except SyntaxError as e:
            res = f"Something went wrong [{e!r}]"
        await callback.message.edit("Calculate here:\n‎" + res, reply_markup=Keyboards.calculator.value)
    else:
        await callback.message.edit(callback.message.text + callback.data, reply_markup=Keyboards.calculator.value)
