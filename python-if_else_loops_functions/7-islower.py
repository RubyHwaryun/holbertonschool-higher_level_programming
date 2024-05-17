#!/usr/bin/python3
def islower(c):
    if ord('a') <= ord('c') <= ord('z'):
        print("{} => lower".format(c))
    elif ord('A') <= ord(c) <= ord('Z'):
        print("{} => upper".format(c))
    else:
        return False
