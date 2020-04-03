# -*- coding:utf-8 -*-

"""Command line interface."""

import prompt

empty_string = ''


def take_user_name() -> str:
    """Greet user and return taken name."""
    print(empty_string)
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print(empty_string)
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


def colour_to_red(text: str) -> str:
    """Colour text to red."""
    font_red = '\033[91m'
    font_end = '\033[0m'
    return '{0}{1}{2}'.format(font_red, text, font_end)


def colour_to_blue(text: str) -> str:
    """Colour text to blue."""
    font_blue = '\033[96m'
    font_end = '\033[0m'
    return '{0}{1}{2}'.format(font_blue, text, font_end)


def colour_to_bold(text: str) -> str:
    """Colour text to bold."""
    font_bold = '\033[1m'
    font_end = '\033[0m'
    return '{0}{1}{2}'.format(font_bold, text, font_end)


def print_if_lose_game(name: str, user_answer: str, correct_answer: str):
    """End game with wrong answer."""
    message = empty_string.join((
        colour_to_red("'{0}'").format(user_answer),
        ' is wrong answer ;',
        colour_to_bold('('),
        colour_to_blue('.'),
        ' Correct answer was ',
        colour_to_red("'{0}'").format(correct_answer),
        colour_to_blue('.\n'),
        'Let',
        colour_to_red("'s try again, {0}!").format(name),
    ))
    print(message)


def print_if_right_answer():
    """Notify user about right answer."""
    print('Correct!')


def print_if_win_game(name: str):
    """End game with right answers."""
    print('Congratulation, {0}!'.format(name))


def print_start_message():
    """Show start message."""
    print('Welcome to the Brain Games!')


def print_calc_rules():
    """Show calc game rules."""
    rules = 'What is the result of the expression?'
    print(rules)


def print_even_rules():
    """Show even game rules."""
    rules = empty_string.join((
        'Answer',
        colour_to_red(' "yes" '),
        colour_to_bold('if'),
        ' number is even otherwise answer ',
        colour_to_red('"no"'),
        colour_to_bold('.'),
    ))
    print(rules)


def print_gcd_rules():
    """Show gcd game rules."""
    rules = 'Find the greatest common divisor of given numbers.'
    print(rules)


def print_prime_rules():
    """Show prime game rules."""
    rules = empty_string.join((
        'Answer "yes" if given number is prime. ',
        'Otherwise answer "no".',
    ))
    print(rules)


def print_progression_rules():
    """Show progression game rules."""
    rules = empty_string.join((
        'What number is missing ',
        colour_to_bold('in'),
        ' the progression?',
    ))
    print(rules)
