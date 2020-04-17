# -*- coding:utf-8 -*-

"""Game engine logic."""

from brain_games import cli

GAME_ROUNDS_NUMBER = 3


def play_game(game_module, user_name: str = None):
    """Play game."""
    cli.print_rules(game_module.RULES)
    if not user_name:
        user_name = cli.welcome_user()
    for _ in range(GAME_ROUNDS_NUMBER):
        question, correct_answer = game_module.create_game_parameters()
        cli.ask_question(question)
        user_answer = cli.take_str_answer()
        if user_answer != correct_answer:
            cli.print_when_lose_game(
                user_name,
                user_answer,
                correct_answer,
            )
            return
        cli.print_when_right_answer()
    cli.print_when_win_game(user_name)


def select_game():
    """Show available games and return name of selected module."""
    cli.print_available_games()
    available_games_numbers = list(range(1, len(cli.GAMES) + 1))
    game_number = cli.take_int_answer()
    while game_number not in available_games_numbers:
        game_number = cli.take_int_answer()
    return cli.GAMES[game_number - 1][1]
