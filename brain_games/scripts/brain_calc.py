#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Calc game start."""

from brain_games import engine, games


def main():
    """Start game."""
    engine.play_game(games.calc)


if __name__ == '__main__':
    main()
