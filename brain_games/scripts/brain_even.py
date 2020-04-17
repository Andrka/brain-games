#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Even game start."""

from brain_games import engine, games
from brain_games.cli import print_start_message


def main():
    """Start game."""
    print_start_message()
    engine.play_game(games.even)


if __name__ == '__main__':
    main()
