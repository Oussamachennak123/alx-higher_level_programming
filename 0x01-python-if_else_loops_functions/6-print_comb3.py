#!/usr/bin/python3
for me in range(0, 10):
    for e in range(me + 1, 10):
        if me == 8 and e == 9:
            print('89')
        else:
            print('{}{}'.format(me, e), end=", ")
