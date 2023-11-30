#!/usr/bin/python3
if __name__ == "__main__":
    import sys, math
    result = 0
    for k in sys.argv:
        result += int(k)
        print("{}".format(result))
