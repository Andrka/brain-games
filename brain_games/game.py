# -*- coding:utf-8 -*-

"""Game logic."""

from brain_games.cli import (
    print_if_lose_game,
    print_if_right_answer,
    print_if_win_game,
    take_user_name,
)


def play_game(
    create_question,
    take_user_answer,
    user_name: str,
):
    """Play game."""
    if not user_name:
        user_name = take_user_name()
    game_rounds_number = 3
    for _ in range(game_rounds_number):
        correct_answer = create_question()
        user_answer = str(take_user_answer())
        if user_answer != correct_answer:
            print_if_lose_game(
                user_name,
                str(user_answer),
                str(correct_answer),
            )
            return
        print_if_right_answer()
    print_if_win_game(user_name)
