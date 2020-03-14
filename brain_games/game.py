# -*- coding:utf-8 -*-

"""Module is being developed. Game logic."""

from brain_games.cli import (
    end_game_fail,
    end_game_win,
    notify_right,
    welcome_user,
)


def play_game(question_function_name, answer_function_name) -> None:
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
