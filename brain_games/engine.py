# -*- coding:utf-8 -*-

"""Game engine logic."""

from brain_games import cli

GAME_ROUNDS_NUMBER = 3


def play_game(game_module):
    """Play game."""
    cli.print_start_message()
    cli.print_rules(game_module.RULES)
    user_name = cli.welcome_user()
    for _ in range(GAME_ROUNDS_NUMBER):
        question, correct_answer = game_module.create_game_parameters()
        cli.ask_question(question)
        user_answer = cli.take_answer()
        if user_answer != correct_answer:
            cli.print_when_lose_game(
                user_name,
                user_answer,
                correct_answer,
            )
            return
        cli.print_when_right_answer()
    cli.print_when_win_game(user_name)
