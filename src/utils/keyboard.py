import emoji
from telebot import types


def create_keyboard(*keys, row_width=2, resize_keyboard=True):
    """
    Create a keyboard from a list of keys.

    Example:
        keys = ['a', 'b', 'c']
    """

    markup = types.ReplyKeyboardMarkup(
        row_width=row_width, 
        resize_keyboard=resize_keyboard
    )

    keys = map(emoji.emojize, keys)
    bottons = map(types.KeyboardButton, keys)
    markup.add(*bottons)

    return markup
