#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    m = 0
    if len(argv) == 1:
        print("0")
    else:
        for i in range(1, len(argv)):
            m += int(argv[i])
        print(m)
