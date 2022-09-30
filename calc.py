def calc(a, b, sign):
    if sign == '+':
        return a + b
    elif sign == '-':
        return a - b
    elif sign == '*':
        return a * b
    elif sign == '/' and b != 0:
        return a / b
    elif sign == '//' and b != 0:
        return a // b
    elif sign == '%' and b != 0:
        return a % b
    else:
        print('Input error')


def if_sign(s):
    return s in ['+', '-', '*', '/', '(', ')']


def split_numbers(num):
    num = num.split()
    num = ''.join(num)  # Эти две строки удаляют все пробелы
    num = num.replace(':', '/')
    add_num = []
    tmp_num = ''
    for i in range(len(num)):
        if num[i].isdigit():
            tmp_num += num[i]
            if i == len(num) - 1:
                add_num.append(int(tmp_num))
        else:
            if num[i - 1].isdigit():
                if tmp_num != '':
                    add_num.append(int(tmp_num))
                tmp_num = ''
            if if_sign(num[i]):
                add_num.append(num[i])
            else:
                return 'Input error.'
    return add_num


def math_operation(num_list, action_1, action_2):
    for i in range(len(num_list) - 1):
        if num_list[i] == action_1 or num_list[i] == action_2:
            tmp_res = calc(num_list[i - 1], num_list[i + 1], num_list[i])
            num_list[i - 1] = tmp_res
            num_list.pop(i + 1)
            num_list.pop(i)
            return num_list


def calc_all(num_list):
    if num_list == 'Input error.':
        return num_list
    while '*' in num_list or '/' in num_list:
        num_list = math_operation(num_list, '*', '/')
    while '+' in num_list or '-' in num_list:
        num_list = math_operation(num_list, '+', '-')
    return num_list


def open_brackets(num_list):
    if num_list == 'Input error.':
        return num_list
    if num_list.count('(') != num_list.count(')'):
        return 'Input error.'
    while '(' in num_list:
        first_num = 0
        for i in range(len(num_list)):
            if num_list[i] == '(':
                first_num = i
            if num_list[i] == ')':
                second_num = i
                first_list = num_list[:first_num]
                second_list = calc_all(num_list[first_num + 1: second_num])
                third_list = num_list[second_num + 1:]
                num_list = first_list + second_list + third_list
                break
    return num_list


def super_calc(input_numbers):
    num_list = split_numbers(input_numbers)  # Разбиваем строку с примером на список
    num_list = open_brackets(num_list)  # Открываем скобки
    num_list = calc_all(num_list)  # Считаем выражение
    # num_list = str(*num_list)
    return num_list

#
# numbers = '5*(5+4)+3*(4+7*(11/5))-7/(99-71)'
# result = super_calc(numbers)
# print('{} = {}'.format(numbers, *result))
