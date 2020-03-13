# -*- coding:utf-8 -*-

"""Module is being developed. General script - game selecting."""

from brain_games.cli import welcome_user


def main() -> None:
    """Start application."""
    print('Welcome to the Brain Games!')  # noqa: T001
    name = welcome_user()  # noqa: F841


if __name__ == '__main__':
    main()
