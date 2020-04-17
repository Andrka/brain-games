#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Calc game start."""

from brain_games import engine, games
from brain_games.cli import print_start_message


def main():
    """Start game."""
    print_start_message()
    engine.play_game(games.calc)


if __name__ == '__main__':
    main()
