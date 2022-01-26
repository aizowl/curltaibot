import re
from telegram import (Update, InlineKeyboardButton, InlineKeyboardMarkup, chat, keyboardbutton,
                      replymarkup, )

from telegram.callbackquery import CallbackQuery
from telegram.ext import (
    CallbackContext,
    Updater,
    CommandHandler,
    PicklePersistence,
    Filters,
    MessageHandler,
    CallbackQueryHandler
)
from telegram.messageentity import MessageEntity
from menup import uslugi_menu_keyboard, main_menu_keyboard
from cr import TOKEN
from kb import tele_buttons, uslugi_menu
from message import text1, text2, text4, text5, text6, text7


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Вас приветствует специальный бот обслуживания Curltai Music. Выберите действие. '.format(
            username=update.effective_user.first_name \
                if update.effective_user.first_name is not None \
                else update.effective_user.username
        ),
        reply_markup=main_menu_keyboard()
    )


MUSIC_REGEX = r'(?=(' + (tele_buttons[0]) + r'))'
IDEA_REGEX = r'(?=(' + (tele_buttons[1]) + r'))'
USLUGI_REGEX = r'(?=(' + (tele_buttons[2]) + r'))'
SVYAZ_REGEX = r'(?=(' + (tele_buttons[3]) + r'))'
STATYA_REGEX = r'(?=(' + (tele_buttons[4]) + r'))'
DM_REGEX = r'(?=(' + (uslugi_menu[0]) + r'))'
YT_REGEX = r'(?=(' + (uslugi_menu[1]) + r'))'


def music(update: Update, context: CallbackContext):
    info = re.match(MUSIC_REGEX, update.message.text)
    update.message.reply_text(
        text1
    )


# def idea(update: Update, context: CallbackContext):
#     info = re.match(IDEA_REGEX, update.message.text)
#     update.message.reply_text(
#         text2
#     )

def zapisat(update: Update, context:CallbackContext):
    z = update.message.text

    print(z[:10])
    if z[:10] == 'Предложить':
        context.bot.send_message(
            chat_id = '@CurltaiChat',
            text = z
        )


def zapis(update: Update, context: CallbackContext):
    info=re.match(IDEA_REGEX, update.message.text)
    update.message.reply_text(
        text2
    )

def svyaz(update: Update, context: CallbackContext):
    info = re.match(SVYAZ_REGEX, update.message.text)
    update.message.reply_text(
        text4
    )


def statya(update: Update, context: CallbackContext):
    info = re.match(STATYA_REGEX, update.message.text)
    update.message.reply_text(
        text5
    )


def receive_uslugi_menu(update: Update, context: CallbackContext):
    info = re.match(USLUGI_REGEX, update.message.text)
    keyboard = [
        [InlineKeyboardButton("Узнать о дистрибуции музыки", callback_data='st1')],
        [InlineKeyboardButton("Узнать об услуге менеджер youtube канала", callback_data='st2')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
         'Выберите действие: ',
         reply_markup=reply_markup
    )


def inline_buttons(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    if query.data == 'st1':
        query.message.reply_text(
            text='''

Дистрибуция музыки на стриминговые платформы всего Мира становится хорошим источником дохода
 и способом продвижения для музыкантов любого уровня и жанра. Работая с нами, вы получаете не только
 качественный сервис по дистрибуции, но и становитесь частью большой команды.
Curltai – это большое сообщество людей, зараженных творчеством.
''',

        )
    if query.data == 'st2':
        query.message.reply_text(
            text='''
Каждый артист сегодня, должен иметь свой youtube канал.
 Канал нужно постоянно оптимизировать, следить за его оформлением, продвигать его.
 Хороший канал приносит доход и служит большой площадкой для продвижения в Мир.

Мы предлагаем Вам предоставить эту работу нам.
Канал будет принадлежать вам и откроется на вашу почту.
Мы лишь будем заниматься его обслуживанием и получать свои 30%.

Будем заливать видео, писать описание, делать обложки, превью, общаться с подписчиками,
ежемесячно отчитываться и так далее. Если хотите воспользоваться этой услугой, то напишите ваше имя,
 вид деятельности и наш менеджер свяжется с вами.
''',
            # reply_markup=uslugi_menu()
        )



updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(USLUGI_REGEX),
    receive_uslugi_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(MUSIC_REGEX),
    music
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(IDEA_REGEX),
    zapis
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(SVYAZ_REGEX),
    svyaz
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(STATYA_REGEX),
    statya
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.text, 
    zapisat
))
updater.dispatcher.add_handler(CallbackQueryHandler(inline_buttons))

updater.start_polling()
updater.idle()
