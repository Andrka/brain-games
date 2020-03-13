# -*- coding:utf-8 -*-

"""Module is being developed. Logic of calc game."""

from random import randint

from brain_games.cli import end_game_fail, take_int_answer, welcome_user


def play_calc() -> None:  # noqa: WPS210
    """Ask user about operation result."""
    name = welcome_user()
    for index in range(3):  # noqa: B007
        first_number = randint(1, 100)  # noqa: S311
        second_number = randint(1, 100)  # noqa: S311
        operation_int = randint(1, 3)  # noqa: S311
        if operation_int == 1:
            operator = '+'
            correct_answer = first_number + second_number
        elif operation_int == 2:
            operator = '-'
            correct_answer = first_number - second_number
        else:
            operator = '*'
            correct_answer = first_number * second_number
        print('Question: {0} {1} {2}'.format(str(first_number), operator, str(second_number)))  # noqa: T001, E501
        answer = take_int_answer()
        if answer != correct_answer:
            end_game_fail(name, str(answer), str(correct_answer))
            return
        print('Correct!')  # noqa: T001
    print('Congratulation, {0}!'.format(name))  # noqa: T001
