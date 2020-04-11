# -*- coding:utf-8 -*-

"""Logic of progression game."""

from random import randint

RULES = 'What number is missing in the progression?'


def create_game_parameters() -> tuple:
    """Create parameters for game round.

    Create and return question and right answer
    for progression game.

    """
    start_number = randint(1, 10)
    step_number = randint(1, 10)
    miss_number_index = randint(0, 9)
    numbers = []
    for index in range(10):
        if index == miss_number_index:
            numbers.append('..')
        else:
            numbers.append(str(start_number + index * step_number))
    return (
        ' '.join(numbers),
        str(start_number + miss_number_index * step_number),
    )
