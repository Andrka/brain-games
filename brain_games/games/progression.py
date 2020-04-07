# -*- coding:utf-8 -*-

"""Logic of progression game."""

from random import randint

from brain_games.cli import paint_to_bold

EMPTY_STRING = ''
RULES = EMPTY_STRING.join((
    'What number is missing ',
    paint_to_bold('in'),
    ' the progression?',
))


def find_progression_number(
    start_number: int,
    step_number: int,
    miss_number: int,
) -> int:
    """Find miss progression number."""
    return start_number + (miss_number - 1) * step_number


def create_round_parameters() -> tuple:
    """Create round parameters.

    Create and return round question and right answer
    for progression game.

    """
    start_number = randint(1, 10)
    step_number = randint(1, 10)
    miss_number = randint(1, 10)
    question = ''
    for index in range(10):
        if (index + 1) == miss_number:
            question = EMPTY_STRING.join((question, '..'))
        else:
            question = EMPTY_STRING.join((
                question,
                str(start_number + index * step_number),
            ))
        if index < 9:
            question = EMPTY_STRING.join((question, ' '))
    return question, find_progression_number(
        start_number,
        step_number,
        miss_number,
    )
