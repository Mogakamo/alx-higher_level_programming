#!/usr/bin/python3
def print_last_digit(number):
    for i in number:
        print("{}".format(i[:-1]), end="")
