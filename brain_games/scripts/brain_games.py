#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""General script."""

from brain_games.cli import print_start_message, welcome_user


def main():
    """Start application."""
    print_start_message()
    welcome_user()


if __name__ == '__main__':
    main()
