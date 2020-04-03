# -*- coding:utf-8 -*-

"""Logic of gcd game."""

from random import randint

from brain_games.cli import ask_question, take_int_answer
from brain_games.game import play_game


def find_gcd(first_number: int, second_number: int) -> int:
    """Find gcd."""
    if second_number == 0:
        return first_number
    return find_gcd(
        second_number,
        first_number % second_number,  # noqa: S001
    )


def create_gcd_question() -> str:
    """Create, show to user numbers and return their gcd."""
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    phrase = '{0} {1}'.format(str(first_number), str(second_number))
    ask_question(phrase)
    correct_answer = find_gcd(first_number, second_number)
    return str(correct_answer)


def play_gcd(user_name: str = ''):
    """Play gcd game."""
    play_game(create_gcd_question, take_int_answer, user_name)
