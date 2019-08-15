from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import telegram
import logging
import os
from os.path import join, dirname

TOKEN='<Insira aqui seu token>'

logging.basicConfig(level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

env = os.environ.get('ENV', 'development')

try:
    def echo(bot, update):
        texto = update.message.text[::-1] + '<b> xaxa oioi</b>'
        print(texto)
        print(update.message.from_user.username)

        bot.send_message(chat_id=update.message.chat_id, text=texto, parse_mode=telegram.ParseMode.HTML)

    echo_handler = MessageHandler(Filters.text, echo)
    dispatcher.add_handler(echo_handler)

    if(env == 'production'):
        PORT = int(os.environ.get('PORT', '5000'))
        HEROKU_APP = os.environ.get('HEROKU_APP')
        logger.info("PORT: " + str(PORT))
        logger.info("HEROKU_APP: " + HEROKU_APP)
        updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
        updater.bot.set_webhook("https://"+ HEROKU_APP +".herokuapp.com/" + TOKEN)
        updater.idle()
    else:
        updater.start_polling()
except Exception as e:
    print(e)