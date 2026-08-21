#!/usr/bin/python3


def uppercase(str):
    for i, c in enumerate(str):
        print("{:c}".format(ord(c) - 32 if 'a' <= c <= 'z' else ord(c)),
              end="\n" if i == len(str) - 1 else "")
    if len(str) == 0:
        print()
