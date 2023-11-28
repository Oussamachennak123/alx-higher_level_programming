#!/usr/bin/python3
for ASCII in range(97, 123):
    if chr(ASCII) != 'q' and chr(ASCII) != 'e':
        print("{}".format(chr(ASCII)), end="")
