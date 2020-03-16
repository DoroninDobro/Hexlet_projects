#!/usr/bin/env python3
from gendiff import cli
from gendiff import engine


def main():
    args = cli.run()
    engine.starter(args)


if __name__ == '__main__':
    main()
