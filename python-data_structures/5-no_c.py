#!/usr/bin/python3

def no_c(my_string):
    for i in range(len(my_string) - 1, -1, -1):
        if my_string[i] == "c":
            my_string = my_string[:i] + my_string[i+1:]
        if my_string[i] == "C":
            my_string = my_string[:i] + my_string[i+1:]
    return my_string
