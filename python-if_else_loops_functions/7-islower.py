#!/usr/bin/python3
def islower(c):
    if ord('A') <= ord(c) <= ord('Z'):
        print("{} => upper".format(c))
    elif ord('a') <= ord('c') <= ord('z'):
        print("{} => lower".format(c))
    else:
        return False
