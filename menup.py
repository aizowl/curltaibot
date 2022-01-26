import telegram
from kb import tele_buttons, uslugi_menu


 
def main_menu_keyboard():

    keyboard=([
        [
            telegram.KeyboardButton(tele_buttons[0]),
            telegram.KeyboardButton(tele_buttons[1]),
        ],
        [
            telegram.KeyboardButton(tele_buttons[2]),
        ],
        [
            telegram.KeyboardButton(tele_buttons[3]),
            telegram.KeyboardButton(tele_buttons[4]),
        ]
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False

    )


def uslugi_menu_keyboard():

    keyboard=([
        [
            telegram.KeyboardButton(uslugi_menu[0]),
            telegram.KeyboardButton(uslugi_menu[1]),
            
        ]
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False

    )
