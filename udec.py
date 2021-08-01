#!/usr/bin/env python3
from argparse import ArgumentParser
from sys import stdin, stdout
from urllib.parse import unquote as url_decode


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("string", nargs="*")
    args = parser.parse_args()

    if args.string:
        stdout.write(url_decode(" ".join(args.string)))
    else:
        stdout.write(url_decode(stdin.read()[:-1]))
