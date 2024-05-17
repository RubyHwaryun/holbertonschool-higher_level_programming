#!/usr/bin/python3
def islower(c):
    if ord('A') <= ord(c) <= ord('Z'):
        print("{} is upper".format(c))
    elif ord('a') <= ord('c') <= ord('z'):
        print("{} is lower".format(c))
    else:
        return False
