# -*- coding: utf8 -*-
from termcolor import colored, cprint

count_questions = 0
count_success = 0
count_fail = 0

d = {
    "Какая версия языка сейчас актуальна? ": "python3",
    "Какая кодировка используется в тексте? ": "utf8",
    "Какой оператор сравнения нужно использовать для работы с None и bool? ": "is",
    "Сколько значений есть у bool? ": "2",
    "Что будет есть случайно умножить None на число? ": "ошибка",
    "Чему равно len('abc')? ": "3",
    "Какой цикл чаще используется? ": "for",
    "Можно ли назвать свою переменную False? ": "нет",
    "Что будет результатом выражение 3 == 3.0? ": "true",
    "Как форматировать строку? ": ".format"
}

for question,answer in d.items():
    a = colored(question,'red',attrs=['bold'])
    cprint(f'Вопрос №{count_questions+1}:','magenta', attrs=['bold','underline'])
    b = input(f'\t{a}')
    if answer == b.lower():
        count_questions += 1
        count_success += 1
        cprint(f'Ответ №{count_questions}:', 'magenta', attrs=['bold','underline'], end = ' '),cprint(f'{b}', 'green', attrs=['bold'], end = ' '), cprint(f'Верно','green', attrs=['reverse', 'blink'])
    if answer != b.lower():
        count_questions += 1
        count_fail += 1
        cprint(f'Ответ №{count_questions}:', 'magenta', attrs=['bold', 'underline'], end=' '), cprint(f'{b}', 'green',attrs=['bold'],end=' '), cprint(f'Ошибка', 'red', attrs=['reverse', 'blink'])

print()
cprint('Статистика:', 'magenta', attrs=['bold','underline'])
cprint(f'Общее кол-во вопросов:     ', 'blue',end=' '),cprint(f'{count_questions}','blue', attrs=['reverse', 'blink'])
cprint(f'Кол-во успешных ответов:   ', 'green', end=' '),cprint(f'{count_success}','green', attrs=['reverse', 'blink'])
cprint(f'Кол-во ответов с ошибками: ', 'red', end=' '),cprint(f'{count_fail}','red', attrs=['reverse', 'blink'])