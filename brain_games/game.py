# -*- coding:utf-8 -*-

"""Module is being developed. Game logic."""

from brain_games.cli import (
    end_game_fail,
    end_game_win,
    notify_right,
    welcome_user,
)


def play_game(question_function_name: object, answer_function_name: object, name: str) -> None:  # noqa: E501
    """Play game.

    # noqa: DAR101

    """
    if not name:
        name = welcome_user()
    game_number_rounds = 3
    for index in range(game_number_rounds):  # noqa: B007
        correct_answer = question_function_name()
        answer = str(answer_function_name())
        if answer != correct_answer:
            end_game_fail(name, str(answer), str(correct_answer))
            return
        notify_right()
    end_game_win(name)
