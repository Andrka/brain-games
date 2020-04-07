# -*- coding:utf-8 -*-

"""Game logic."""

from brain_games.cli import (
    ask_question,
    print_rules,
    print_start_message,
    print_when_lose_game,
    print_when_right_answer,
    print_when_win_game,
    take_int_answer,
    take_str_answer,
    welcome_user,
)

GAME_ROUNDS_NUMBER = 3


def play_game(game_module):
    """Play game."""
    print_start_message()
    print_rules(game_module.RULES)
    user_name = welcome_user()
    for _ in range(GAME_ROUNDS_NUMBER):
        question, correct_answer = game_module.create_round_parameters()
        ask_question(question)
        if isinstance(correct_answer, int):
            user_answer = take_int_answer()
        else:
            user_answer = take_str_answer()
        if user_answer != correct_answer:
            print_when_lose_game(
                user_name,
                user_answer,
                correct_answer,
            )
            return
        print_when_right_answer()
    print_when_win_game(user_name)
