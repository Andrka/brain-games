# -*- coding:utf-8 -*-

"""Logic of prime game."""

from random import randint

from brain_games.cli import ask_question, take_str_answer
from brain_games.game import play_game


def check_if_prime(number: int) -> str:
    """Check number for prime."""
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


def create_prime_question() -> str:
    """Create, show to user number and return if it is prime."""
    number = randint(1, 1000)
    phrase = str(number)
    ask_question(phrase)
    return check_if_prime(number)


def play_prime(user_name: str = ''):
    """Play prime game."""
    play_game(create_prime_question, take_str_answer, user_name)
