# -*- coding:utf-8 -*-

"""Module is being developed. Logic of even game."""

from random import randint

from brain_games.cli import (
    font_blue,
    font_bold,
    font_end,
    font_red,
    take_answer,
    take_name,
)


def play_even() -> None:  # noqa: WPS213
    """Ask user about numbers type."""
    name = take_name()
    print('Hello, {0}!'.format(name))  # noqa: T001
    print('')  # noqa: T001
    for index in range(3):  # noqa: B007
        quiz_number = randint(1, 100)  # noqa: S311
        if quiz_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print('Question: {0}'.format(str(quiz_number)))  # noqa: T001
        answer = take_answer()
        if correct_answer != answer:
            print('{0}\'{1}\'{2} is wrong '.format(font_red, answer, font_end), end='')  # noqa: T001, E501, Q003
            print('answer ;{0}({1}{2}.{3} '.format(font_bold, font_end, font_blue, font_end), end='')  # noqa: T001, E501
            print('Correct answer was ', end='')  # noqa: T001
            print('{0}\'{1}\'{2}{3}.{4}'.format(font_red, correct_answer, font_end, font_blue, font_end))  # noqa: T001, E501, Q003
            print('Let{0}\'s try again, '.format(font_red), end='')  # noqa: T001, E501, Q003
            print('{0}!{1}'.format(name, font_end))  # noqa: T001
            return
        print('Correct!')  # noqa: T001
    print('Congratulation, {0}!'.format(name))  # noqa: T001
