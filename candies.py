from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from emoji import emojize
from random import randint




def draw_candies(count):
    print('Осталось конфет: ' + str(count))
    candy = emojize(':candy:') + ' '
    while count > 10:
        print(candy * 10)
        count -= 10
    print(candy * count)


def take_input(player_answer, min_num, max_num, num_of_cand):
    # while True:

    if not player_answer.isdigit():
        return 'Некорректный ввод. Вы уверены, что ввели число?'
    player_answer = int(player_answer)
    if min_num <= player_answer <= max_num:
        if player_answer <= num_of_cand:
            return str(player_answer)
        else:
            return 'Осталось меньше конфет, чем ты хочешь взять!'
    else:
        return 'Некорректный ввод. Введите число от {} до {}.'.format(min_num, max_num)


def computer_turn(min_num, max_num, num_of_cand):
    best_turn = num_of_cand % (max_num + 1)
    if best_turn == 0:
        best_turn = randint(min_num, max_num)
    return best_turn


def player_vs_player(min_take, max_take, number_of_candies):
    draw_candies(number_of_candies)
    move = 1
    while number_of_candies > 0:
        if move:
            player_take = take_input(1, min_take, max_take, number_of_candies)
            number_of_candies -= player_take
            if number_of_candies == 0:
                print('\nПобедил игрок 1! ' + emojize(':1st_place_medal:'))
                break
            draw_candies(number_of_candies)
            move = 0
        else:
            player_take = take_input(2, min_take, max_take, number_of_candies)
            number_of_candies -= player_take
            if number_of_candies == 0:
                print('\nПобедил игрок 2! ' + emojize(':1st_place_medal:'))
                break
            draw_candies(number_of_candies)
            move = 1


def player_vs_computer(move, min_take=1, max_take=3, number_of_candies=10):
    draw_candies(number_of_candies)
    # move = int(input('Введите 1, если хотите ходить первым, и 2 - если вторым: '))

    while number_of_candies > 0:
        if move == 1:
            player_take = take_input(1, min_take, max_take, number_of_candies)
            number_of_candies -= player_take
            if number_of_candies == 0:
                print('\nТы победил! ' + emojize(':1st_place_medal:'))
                break
            draw_candies(number_of_candies)
            move = 2
        else:
            computer_take = computer_turn(min_take, max_take, number_of_candies)
            number_of_candies -= computer_take
            if number_of_candies == 0:
                print('\nПобедил компьютер! ' + emojize(':laptop:') + emojize(':1st_place_medal:'))
                break
            draw_candies(number_of_candies)
            move = 1

# def start(msg, min_take=1, max_take=3, number_of_candies=10):
#     game = int(msg)
#     if game == 1:
#         player_vs_computer(min_take, max_take, number_of_candies)
#     else:
#         player_vs_player(min_take, max_take, number_of_candies)


# start()
