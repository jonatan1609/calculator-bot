from enum import Enum
from pyrogram import filters, types


class Filters(Enum):
    START = filters.private & filters.command('start')


class Messages(Enum):
    START = "Hi {name}, welcome.\nHere you can calculate your stuff."


class Keyboards(Enum):
    calculator = types.InlineKeyboardMarkup([
        [types.InlineKeyboardButton(str(i), str(i)) for i in "/*|&^%"],
        [types.InlineKeyboardButton(str(i), str(i)) for i in range(7, 10)] + [types.InlineKeyboardButton("+", "+")],
        [types.InlineKeyboardButton(str(i), str(i)) for i in range(4, 7)] + [types.InlineKeyboardButton("-", "-")],
        [types.InlineKeyboardButton(str(i), str(i)) for i in range(1, 4)] + [types.InlineKeyboardButton(".", ".")],
        [types.InlineKeyboardButton("0", "0")],
        [types.InlineKeyboardButton("=", "="), types.InlineKeyboardButton("C", "C"),]
    ])
