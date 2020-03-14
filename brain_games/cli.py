# -*- coding:utf-8 -*-

"""Module is being developed. Command line interface."""

import prompt

font_red = '\033[91m'
font_blue = '\033[96m'
font_bold = '\033[1m'
font_end = '\033[0m'


def take_name() -> str:
    """Take user name.

    # noqa: DAR201

    """
    return prompt.string('May I have your name? ')


def welcome_user() -> str:
    """Greet user and return name.

    # noqa: DAR201

    """
    print('')  # noqa: T001
    name = take_name()
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


def end_game_fail(name: str, answer: str, correct_answer: str) -> None:
    """End game with wrong answer.

    # noqa: DAR101

    """
    print('{0}\'{1}\'{2} is wrong '.format(font_red, answer, font_end), end='')  # noqa: T001, E501, Q003
    print('answer ;{0}({1}{2}.{3} '.format(font_bold, font_end, font_blue, font_end), end='')  # noqa: T001, E501
    print('Correct answer was ', end='')  # noqa: T001
    print('{0}\'{1}\'{2}{3}.{4}'.format(font_red, correct_answer, font_end, font_blue, font_end))  # noqa: T001, E501, Q003
    print('Let{0}\'s try again, '.format(font_red), end='')  # noqa: T001, E501, Q003
    print('{0}!{1}'.format(name, font_end))  # noqa: T001


def notify_right() -> None:
    """Notify user about right answer."""
    print('Correct!')  # noqa: T001


def end_game_win(name: str) -> None:
    """End game with right answers.

    # noqa: DAR101

    """
    print('Congratulation, {0}!'.format(name))  # noqa: T001


def game(question_function_name, answer_function_name) -> None:
    """Play game.

    # noqa: DAR101

    """
    name = welcome_user()
    for index in range(3):  # noqa: B007
        correct_answer = question_function_name()
        answer = str(answer_function_name())
        if answer != correct_answer:
            end_game_fail(name, str(answer), str(correct_answer))
            return
        notify_right()
    end_game_win(name)
