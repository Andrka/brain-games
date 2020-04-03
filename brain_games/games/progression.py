# -*- coding:utf-8 -*-

"""Logic of progression game."""

from random import randint

from brain_games.cli import ask_question, take_int_answer
from brain_games.game import play_game


def find_progression_number(
    start_number: int,
    step_number: int,
    miss_number: int,
) -> int:
    """Find miss progression number."""
    return start_number + (miss_number - 1) * step_number


empty_string = ''


def create_progression_question() -> str:
    """Create, show to user progression and return miss number."""
    start_number = randint(1, 10)
    step_number = randint(1, 10)
    miss_number = randint(1, 10)
    phrase = ''
    for index in range(10):
        if (index + 1) == miss_number:
            phrase = empty_string.join((phrase, '..'))
        else:
            phrase = empty_string.join((
                phrase,
                str(start_number + index * step_number),
            ))
        if index < 9:
            phrase = empty_string.join((phrase, ' '))
    ask_question(phrase)
    return str(find_progression_number(start_number, step_number, miss_number))


def play_progression(user_name: str = empty_string):
    """Play progression game."""
    play_game(create_progression_question, take_int_answer, user_name)
