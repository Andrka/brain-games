#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""General script."""

from brain_games import engine
from brain_games.cli import print_start_message, welcome_user


def main():
    """Start application."""
    print_start_message()
    user_name = welcome_user()
    selected_game = engine.select_game()
    engine.play_game(selected_game, user_name)


if __name__ == '__main__':
    main()
