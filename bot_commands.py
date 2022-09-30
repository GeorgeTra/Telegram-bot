from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import time
from log import *
from calc import super_calc
from candies import *
from emoji import emojize

calc_mode_on = False
candies_mode_on = False
game_mode = 0
move_turn = False
number_of_candies = 10
min_take = 1
max_take = 3
game_turn = 0


def help_com(update: Update, context: CallbackContext):
    reply = '/help помощь\n\
    /hello приветствие\n\
    /sum два числа через пробел\n\
    /time текущие дата и время\n\
    /calc_start запуск калькулятора\n\
    /calc_stop остановка калькулятора\n\
    /candies игра в конфетки'
    update.message.reply_text(reply)
    log(update, context, '/help')


def hello(update: Update, context: CallbackContext):
    user_name = update.effective_user.first_name
    if user_name == 'Katerina':
        reply = f'Привет, сладенькая!'
    else:
        reply = f'Привет, {user_name}!'
    update.message.reply_text(reply)
    log(update, context, reply)


def sum_com(update: Update, context: CallbackContext):
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    reply = f'{x} + {y} = {x + y}'
    update.message.reply_text(reply)
    log(update, context, reply)


def time_com(update: Update, context: CallbackContext):
    now = datetime.datetime.now()
    now_time = now.strftime("%d-%m-%Y %H:%M:%S")
    reply = f'{now_time}'
    update.message.reply_text(reply)
    log(update, context, reply)


def calc_start(update: Update, context: CallbackContext):
    update.message.reply_text('Введи пример, и я решу его!')
    global calc_mode_on
    calc_mode_on = True


def calc_stop(update: Update, context: CallbackContext):
    update.message.reply_text('Спасибо за интересные примеры ' + emojize(':thumbs_up:'))
    global calc_mode_on
    calc_mode_on = False


def calc_mode(msg):
    result = super_calc(msg)
    if result == 'Input error.':
        reply = result
        # reply = 'Ошибка ввода. Что-то пошло не так ' \
        #         + emojize(':sad_but_relieved_face:')
        # return result
    else:
        reply = '= {}'.format(*result)
    return reply


def msg_com(update: Update, context: CallbackContext):
    msg = update.message.text
    global number_of_candies
    global game_mode
    global move_turn
    global min_take
    global max_take
    global game_turn
    if calc_mode_on:
        reply = calc_mode(msg)
        update.message.reply_text(reply)
        log(update, context, reply)
    # if candies_mode_on:
    #     if not game_mode:
    #         game_mode = int(msg)
    #         print(f'move_turn_0 = {move_turn}')
    #         print(f'game_turn_0 = {game_turn}')
    #         update.message.reply_text('Введите 1, если хотите ходить первым, и 2 - если вторым:')
    #     elif game_mode == 1:  # против компьютера
    #         if number_of_candies > 0:
    #             if not move_turn:
    #                 move_turn = True
    #                 game_turn = int(msg)
    #                 print(f'move_turn = {move_turn}')
    #                 print(f'game_turn = {game_turn}')
    #                 if game_turn == 1:
    #                     update.message.reply_text(f'Осталось конфет: {number_of_candies}')
    #                     update.message.reply_text('Сколько конфет возьмешь? ')
    #                 elif game_turn == 2:
    #                     update.message.reply_text(f'Осталось конфет: {number_of_candies}')
    #                     update.message.reply_text('Компьютер думает...')
    #                     time.sleep(5)
    #                     computer_take = computer_turn(min_take, max_take, number_of_candies)
    #                     update.message.reply_text('Компьютер взял конфет: {}.'.format(computer_take))
    #                     number_of_candies -= computer_take
    #                     game_turn = 1
    #                     update.message.reply_text(f'Осталось конфет: {number_of_candies}')
    #                     update.message.reply_text('Сколько конфет возьмешь? ')
    #             elif move_turn:
    #                 if game_turn == 1:
    #                     print(msg)
    #                     print(f'move_turn_1 = {move_turn}')
    #                     print(f'game_turn_1 = {game_turn}')
    #                     player_take = take_input(msg, min_take, max_take, number_of_candies)
    #                     if player_take.isdigit():
    #                         number_of_candies -= int(player_take)
    #                         if number_of_candies == 0:
    #                             update.message.reply_text('Ты победил! ' + emojize(':1st_place_medal:'))
    #                             game_mode = 0
    #                             move_turn = False
    #                             number_of_candies = 10
    #                             game_turn = 0
    #                         else:
    #                             update.message.reply_text(f'Осталось конфет: {number_of_candies}')
    #                             game_turn = 2
    #                     else:
    #                         update.message.reply_text(player_take)
    #                 if game_turn == 2:
    #                     print(msg)
    #                     print(f'move_turn_2 = {move_turn}')
    #                     print(f'game_turn_2 = {game_turn}')
    #                     update.message.reply_text('Компьютер думает...')
    #                     time.sleep(5)
    #                     computer_take = computer_turn(min_take, max_take, number_of_candies)
    #                     update.message.reply_text('Компьютер взял конфет: {}.'.format(computer_take))
    #                     number_of_candies -= computer_take
    #                     if number_of_candies == 0:
    #                         update.message.reply_text(
    #                             'Победил компьютер! ' + emojize(':laptop:') + emojize(':1st_place_medal:'))
    #                         game_mode = 0
    #                         move_turn = False
    #                         number_of_candies = 10
    #                         game_turn = 0
    #                     else:
    #                         update.message.reply_text(f'Осталось конфет: {number_of_candies}')
    #                         update.message.reply_text('Сколько конфет возьмешь? ')
    #                     game_turn = 1
    return msg


def candies(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("С ботом", callback_data='1'),
         InlineKeyboardButton("С другим игроком", callback_data='2')]]
    update.message.reply_text('Начинаем игру!\nВыбери режим игры', reply_markup=InlineKeyboardMarkup(keyboard))
    global calc_mode_on
    calc_mode_on = False
    global candies_mode_on
    candies_mode_on = True


def button(update, context):
    query = update.callback_query
    query.answer()
    global game_mode, move_turn, number_of_candies, min_take, max_take
    if not game_mode:
        if query.data == "1":
            game_mode = 1
            vs_comp(update, context)
        elif query.data == "2":
            context.bot.send_message(update.effective_chat.id,
                                     'Вы выбрали режим игры с другим игроком!')
            game_mode = 2
        context.bot.send_message(update.effective_chat.id,
                                 f'Всего конфет: {number_of_candies}')
    if game_mode == 1:  # против компьютера
        if not move_turn:
            if query.data == "3":
                context.bot.send_message(update.effective_chat.id,
                                         'Вы ходите первым!')
                move_turn = 1
                player_turn(update, context)
            elif query.data == "4":
                context.bot.send_message(update.effective_chat.id,
                                         'Вы ходите вторым!')
                move_turn = 2
        elif move_turn == 1:
            if query.data == "5":
                number_of_candies -= 1
            elif query.data == "6":
                number_of_candies -= 2
            elif query.data == "7":
                number_of_candies -= 3
            if number_of_candies == 0:
                context.bot.send_message(update.effective_chat.id,
                                         'Ты победил! ' + emojize(':1st_place_medal:'))
                game_mode = 0
                move_turn = False
                number_of_candies = 10
            else:
                move_turn = 2
                context.bot.send_message(update.effective_chat.id,
                                         f'Осталось конфет: {number_of_candies}')
        if move_turn == 2:
            context.bot.send_message(update.effective_chat.id, 'Бот думает...')
            # TODO прогресс-бар раздумий
            time.sleep(3)
            computer_take = computer_turn(min_take, max_take, number_of_candies)
            context.bot.send_message(update.effective_chat.id,
                                     'Бот взял конфет: {}.'.format(computer_take))
            number_of_candies -= computer_take
            if number_of_candies == 0:
                context.bot.send_message(update.effective_chat.id,
                                         'Победил бот! ' + emojize(':laptop:') + emojize(':1st_place_medal:'))
                game_mode = 0
                move_turn = False
                number_of_candies = 10
            else:
                move_turn = 1
                context.bot.send_message(update.effective_chat.id,
                                         f'Осталось конфет: {number_of_candies}')
                player_turn(update, context)

    # if game_mode == 2:


# TODO: ПРОТИВ ДРУГОГО ИГРОКА

def vs_comp(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Хочу первым!", callback_data='3'),
         InlineKeyboardButton("Хожу вторым, даю фору", callback_data='4')]]
    context.bot.send_message(update.effective_chat.id,
                             'Вы выбрали режим игры с ботом!\nКто начинает?',
                             reply_markup=InlineKeyboardMarkup(keyboard))


def player_turn(update: Update, context: CallbackContext):
    global number_of_candies
    user_name = update.effective_user.first_name
    if number_of_candies >= 3:
        keyboard = [
            [InlineKeyboardButton("1", callback_data='5'),
             InlineKeyboardButton("2", callback_data='6'),
             InlineKeyboardButton("3", callback_data='7')]]
    if number_of_candies == 2:
        keyboard = [
            [InlineKeyboardButton(f"Беру одну, хочу проиграть {emojize(':clown_face:')}", callback_data='5'),
             InlineKeyboardButton("2", callback_data='6')]]
    if number_of_candies == 1:
        keyboard = [
            [InlineKeyboardButton("Забираю последнюю! Ура!", callback_data='5')]]
    context.bot.send_message(update.effective_chat.id,
                             f'{user_name}, сколько конфет возьмешь?',
                             reply_markup=InlineKeyboardMarkup(keyboard))

# def bot_turn():


# elif query.data == "3":
#     context.bot.send_message(update.effective_chat.id, get_data_from_file("wed.txt"))
# elif query.data == "4":
#     context.bot.send_message(update.effective_chat.id, get_data_from_file("thu.txt"))
# elif query.data == "5":
#     context.bot.send_message(update.effective_chat.id, get_data_from_file("fri.txt"))
# elif query.data == "7":
#     context.bot.send_message(update.effective_chat.id, get_data_from_file("math.txt"))
# elif query.data == "8":
#     context.bot.send_message(update.effective_chat.id, get_data_from_file("rus.txt"))
# elif query.data == "9":
#     context.bot.send_message(update.effective_chat.id, get_data_from_file("lit.txt"))
# elif query.data == "10":
#     context.bot.send_message(update.effective_chat.id, get_data_from_file("eng.txt"))
# else:
#     context.bot.send_message(update.effective_chat.id, "Нет такого дня пока что!")

# def candies_mode(msg, update: Update, context: CallbackContext):
#     global number_of_candies
#     global game_mode
#     global move_turn
#     global min_take
#     global max_take
#     global game_turn
#     game_mode = int(msg)
#     update.message.reply_text('Введите 1, если хотите ходить первым, и 2 - если вторым:')
#     if not game_mode:
#
#         print(f'move_turn_0 = {move_turn}')
#         print(f'game_turn_0 = {game_turn}')
#         update.message.reply_text('Введите 1, если хотите ходить первым, и 2 - если вторым:')


# def calc_com(update: Update, context: CallbackContext):
#     update.message.reply_text('Введи пример, и я решу его!')
#     time.sleep(10)
#     msg = msg_com(Update, CallbackContext)
#     while 'calc' in msg:
#         update.message.reply_text('Давай же, я жду ;)')
#         print(msg)
#         time.sleep(10)
#         msg = msg_com(Update, CallbackContext)
#     # msg = msg.split()
#     # msg.pop(0)
#     # numbers = ''.join(msg)
#     result = calc(msg)
#     reply = '{} = {}'.format(msg, *result)
#     update.message.reply_text(reply)
#     log(update, context, reply)
