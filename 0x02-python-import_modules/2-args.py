#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv)-1 == 0:
        print("0 arguments.")
    elif len(sys.argv)-1 == 1:
        print("1 argument:\n{}: {}".format(len(sys.argv)-1, sys.argv[1]))
    else:
        print("{} arguments:".format(len(sys.argv)-1))
        for a in range(1, len(sys.argv)):
            print("{}: {}".format(a, sys.argv[a]))
