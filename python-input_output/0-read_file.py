#!/usr/bin/python3

def read_file(filename=""):
    with open('my_file', encoding="utf-8") as f:
	read_data = f.read()
    f.closed
