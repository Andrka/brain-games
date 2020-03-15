#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Module is being developed. General script - game selecting."""

from brain_games.cli import show_start_message, welcome_user


def main() -> None:
    """Start application."""
    show_start_message()
    name = welcome_user()  # noqa: F841


if __name__ == '__main__':
    main()
