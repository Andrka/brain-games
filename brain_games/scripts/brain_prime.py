#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Prime game start."""

from brain_games import engine, games


def main():
    """Start game."""
    engine.play_game(games.prime)


if __name__ == '__main__':
    main()
