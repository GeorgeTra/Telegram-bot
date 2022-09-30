from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime


def log(update: Update, context: CallbackContext, reply=''):
    now = datetime.datetime.now()
    now_time = now.strftime("%d-%m-%Y %H:%M:%S")
    file = open('db.csv', 'a')
    file.write(
        f'{now_time};\
        {update.effective_user.first_name};\
        {update.message.text};\
        {reply}\n')
    file.close()
