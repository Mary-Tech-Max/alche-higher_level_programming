#!/usr/bin/python3


def uppercase(str):
    for i, c in enumerate(str):
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            print("{:c}".format(ord(c) - 32),
                  end="\n" if i == len(str) - 1 else "")
        else:
            print("{}".format(c),
                  end="\n" if i == len(str) - 1 else "")
    if len(str) == 0:
        print()
