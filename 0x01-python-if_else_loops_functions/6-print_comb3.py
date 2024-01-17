#!/usr/bin/python3
for num in range(0, 90):
    if num % 10 == 0 and num != 0:
        num += 1 + num // 10
    print("{:02d}".format(num), end='\n' if num == 89 else ", ")
