import os

from django.utils.translation import gettext as _
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Dispatcher, CommandHandler, Handler, \
    CallbackQueryHandler


def start_callback(update, context):
    keyboard = [[InlineKeyboardButton(_('Search news'),
                                      callback_data='search_news'),
                 InlineKeyboardButton("Option 2", callback_data='2')],

                [InlineKeyboardButton("Option 3", callback_data='3')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    context.message.reply_text("You are welcome", reply_markup=reply_markup)


def news_callback(update, context):
    query = context.callback_query
    query.edit_message_text(text="Selected option: {}".format(query.data))


def error(update, context):
    """Log Errors caused by Updates."""
    print('Update "%s" caused error "%s"', update, context.error)


bot = Bot(os.getenv('TELEGRAM_BOT_TOKEN'))

dispatcher = Dispatcher(bot, None, workers=1)
dispatcher.add_handler(CommandHandler("start", start_callback))
dispatcher.add_handler(CallbackQueryHandler(news_callback))
dispatcher.add_error_handler(error)
