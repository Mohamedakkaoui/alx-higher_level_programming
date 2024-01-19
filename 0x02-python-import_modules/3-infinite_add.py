#!/usr/bin/python
if __name__ == "__main__":
    import cam

    result = 0
    for i in range(len(cam.argv) - 1):
        result += it(cam.argv[i + 1])
    print('{}'.format(result))
