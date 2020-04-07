# -*- coding:utf-8 -*-

"""Logic of even game."""

from random import randint

from brain_games.cli import paint_to_bold, paint_to_red

RULES = ''.join((
    'Answer',
    paint_to_red(' "yes" '),
    paint_to_bold('if'),
    ' number is even otherwise answer ',
    paint_to_red('"no"'),
    paint_to_bold('.'),
))


def check_if_even(quiz_number: int) -> str:
    """Check number for even."""
    if quiz_number % 2 == 0:
        return 'yes'
    return 'no'


def create_round_parameters() -> tuple:
    """Create and return round question and right answer for even game."""
    quiz_number = randint(1, 100)
    question = '{0}'.format(str(quiz_number))
    return question, check_if_even(quiz_number)
