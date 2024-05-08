#!/usr/bin/python3
for i in range(100):
  if i < 10:
    print("0" + str(i), end=", ")
  else:
    print(i, end=", ")
