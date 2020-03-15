# -*- coding:utf-8 -*-

"""Module is being developed. Command line interface."""

import prompt


def welcome_user() -> str:
    """Greet user and return taken name.

    # noqa: DAR201

    """
    print('')  # noqa: T001
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))  # noqa: T001
    print('')  # noqa: T001
    return name


def take_str_answer() -> str:
    """Take str answer from user.

    # noqa: DAR201

    """
    return prompt.string('Your answer: ')


def take_int_answer() -> int:
    """Take int answer from user.

    # noqa: DAR201

    """
    return prompt.integer('Your answer: ')


def ask_question(phrase: str) -> None:
    """Ask user the question.

    # noqa: DAR101

    """
    print('Question: {0}'.format(phrase))  # noqa: T001


FONT_RED = '\033[91m'
FONT_BLUE = '\033[96m'
FONT_BOLD = '\033[1m'
FONT_END = '\033[0m'


def end_game_fail(name: str, answer: str, correct_answer: str) -> None:
    """End game with wrong answer.

    # noqa: DAR101

    """
    print('{0}\'{1}\'{2} is wrong '.format(FONT_RED, answer, FONT_END), end='')  # noqa: T001, E501, Q003
    print('answer ;{0}({1}{2}.{3} '.format(FONT_BOLD, FONT_END, FONT_BLUE, FONT_END), end='')  # noqa: T001, E501
    print('Correct answer was ', end='')  # noqa: T001
    print('{0}\'{1}\'{2}{3}.{4}'.format(FONT_RED, correct_answer, FONT_END, FONT_BLUE, FONT_END))  # noqa: T001, E501, Q003
    print('Let{0}\'s try again, '.format(FONT_RED), end='')  # noqa: T001, E501, Q003
    print('{0}!{1}'.format(name, FONT_END))  # noqa: T001


def notify_right() -> None:
    """Notify user about right answer."""
    print('Correct!')  # noqa: T001


def end_game_win(name: str) -> None:
    """End game with right answers.

    # noqa: DAR101

    """
    print('Congratulation, {0}!'.format(name))  # noqa: T001


def show_start_message() -> None:
    """Show start message."""
    print('Welcome to the Brain Games!')  # noqa: T001


def show_calc_rules() -> None:
    """Show calc game rules."""
    print('What is the result of the exspression?')  # noqa: T001


def show_even_rules() -> None:
    """Show even game rules."""
    print('Welcome to the Brain Games!')  # noqa: T001
    print('Answer {0}"yes"{1} '.format(FONT_RED, FONT_END), end='')  # noqa: T001, E501
    print('{0}if{1} number even otherwise '.format(FONT_BOLD, FONT_END), end='')  # noqa: T001, E501
    print('answer {0}"no"{1}{2}.{3}'.format(FONT_RED, FONT_END, FONT_BLUE, FONT_END))  # noqa: T001, E501


def show_gcd_rules() -> None:
    """Show gcd game rules."""
    print('Find the greatest common divisor of given numbers.')  # noqa: T001


def show_prime_rules() -> None:
    """Show prime game rules."""
    print('Answer "yes" if given number is prime. Otherwise answer "no".')  # noqa: T001, E501


def show_progression_rules() -> None:
    """Show progression game rules."""
    print('What number is missing {0}in{1} the progression?'.format(FONT_BOLD, FONT_END))  # noqa: T001, E501
