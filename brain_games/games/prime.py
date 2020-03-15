# -*- coding:utf-8 -*-

"""Module is being developed. Logic of prime game."""

from random import randint

from brain_games.cli import ask_question, take_str_answer
from brain_games.game import play_game


def check_prime(number: int) -> str:
    """Find number type.

    # noqa: DAR101
    # noqa: DAR201

    """
    if number % 2 == 0:
        if number == 2:
            return 'yes'
        return 'no'
    divisor = 3
    while divisor ** 2 <= number and number % divisor != 0:  # noqa: S001
        divisor += 2
    if divisor ** 2 > number:
        return 'yes'
    return 'no'


def realise_prime_question() -> str:  # noqa: WPS210
    """Realise prime.

    # noqa: DAR201

    """
    number = randint(1, 1000)  # noqa: S311
    phrase = str(number)
    ask_question(phrase)
    correct_answer = check_prime(number)
    return correct_answer  # noqa: WPS331


def play_prime(name: str = '') -> None:
    """Play prime game.

    # noqa: DAR101

    """
    play_game(realise_prime_question, take_str_answer, name)
