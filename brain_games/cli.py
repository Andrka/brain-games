# -*- coding:utf-8 -*-

"""Command line interface."""

import prompt


def welcome_user() -> str:
    """Greet user and return taken name."""
    print('')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print('')
    return name


def take_str_answer() -> str:
    """Take answer with str type from user."""
    return prompt.string('Your answer: ')


def take_int_answer() -> int:
    """Take answer with int type from user."""
    return prompt.integer('Your answer: ')


def ask_question(phrase: str):
    """Ask user the question."""
    print('Question: {0}'.format(phrase))


FONT_RED = '\033[91m'
FONT_END = '\033[0m'


def paint_to_red(text: str) -> str:
    """Paint text to red."""
    return '{0}{1}{2}'.format(FONT_RED, text, FONT_END)


FONT_BLUE = '\033[96m'


def paint_to_blue(text: str) -> str:
    """Paint text to blue."""
    return '{0}{1}{2}'.format(FONT_BLUE, text, FONT_END)


FONT_BOLD = '\033[1m'


def paint_to_bold(text: str) -> str:
    """Paint text to bold."""
    return '{0}{1}{2}'.format(FONT_BOLD, text, FONT_END)


def print_when_lose_game(name: str, user_answer, correct_answer):
    """End game with wrong answer."""
    message = ''.join((
        paint_to_red("'{0}'").format(user_answer),
        ' is wrong answer ;',
        paint_to_bold('('),
        paint_to_blue('.'),
        ' Correct answer was ',
        paint_to_red("'{0}'").format(correct_answer),
        paint_to_blue('.\n'),
        'Let',
        paint_to_red("'s try again, {0}!").format(name),
    ))
    print(message)


def print_when_right_answer():
    """Notify user about right answer."""
    print('Correct!')


def print_when_win_game(name: str):
    """End game with right answers."""
    print('Congratulation, {0}!'.format(name))


def print_start_message():
    """Show start message."""
    print('\nWelcome to the Brain Games!')


def print_rules(rules: str):
    """Show game rules."""
    print(rules)
