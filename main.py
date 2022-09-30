from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, ConversationHandler, MessageHandler, Filters, \
    CallbackQueryHandler
from bot_commands import *

NUM = 1
updater = Updater('5368167469:AAFtQUat0bg88ktTfY08zs-nCCvtnped274')
print('Bot started')
global dispatcher
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('help', help_com))
dispatcher.add_handler(CommandHandler('hello', hello))
dispatcher.add_handler(CommandHandler('sum', sum_com))
dispatcher.add_handler(CommandHandler('time', time_com))
dispatcher.add_handler(CommandHandler('calc_start', calc_start))
dispatcher.add_handler(CommandHandler('calc_stop', calc_stop))
dispatcher.add_handler(CommandHandler('candies', candies))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, msg_com))
dispatcher.add_handler(CallbackQueryHandler(button))

# calc_handler = ConversationHandler(
#     entry_points=[CommandHandler('calc', calc_start)],
#     states={NUM: [MessageHandler(Filters.text & ~Filters.command, calc_com)]},
#     fallbacks=[CommandHandler('cancel', calc_cancel)],
# )

updater.start_polling()
updater.idle()
