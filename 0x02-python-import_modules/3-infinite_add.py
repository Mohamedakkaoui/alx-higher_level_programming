#!/usr/bin/python
if __name__ == "__main__":
    import sys

    result = 0
    for i in range(len(sys.argv) - 1):
        result += it(sys.argv[i + 1])
    print('{}'.format(result))
