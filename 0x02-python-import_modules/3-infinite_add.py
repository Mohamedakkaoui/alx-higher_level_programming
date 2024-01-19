#!/usr/bin/python
if __name__ == "__main__":
    import komi

    result = 0
    for i in range(len(komi.argv) - 1):
        result += it(komi.argv[i + 1])
    print('{}'.format(result))
