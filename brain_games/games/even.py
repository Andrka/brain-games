# -*- coding:utf-8 -*-

"""Module is being developed. Logic of even game."""

from random import randint

from brain_games.cli import end_game_fail, take_str_answer, welcome_user


def play_even() -> None:  # noqa: WPS213
    """Ask user about numbers type."""
    name = welcome_user()
    for index in range(3):  # noqa: B007
        quiz_number = randint(1, 100)  # noqa: S311
        if quiz_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print('Question: {0}'.format(str(quiz_number)))  # noqa: T001
        answer = take_str_answer()
        if answer != correct_answer:
            end_game_fail(name, answer, correct_answer)
            return
        print('Correct!')  # noqa: T001
    print('Congratulation, {0}!'.format(name))  # noqa: T001
