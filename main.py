#!/bin/usr/env python 

import random 
import string

lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

allchars = list(string.printable)

pwd = []

def choose():
    print("You have four options!")
    choose = int(input("Which chars to you want to have in your password? [lowercase/uppercase/numbers/all]	     "))
    length = input("How long is your password supposed to be?      ")

    if choose == 1:
        for i in range(int(length)):
            pwd.append(random.choice(lowercase))
        print("".join(pwd))    

    if choose == 2:
        for i in range(int(length)):
            pwd.append(random.choice(uppercase))
        print("".join(pwd))

    if choose == 3:
        for i in range(int(length)):
            pwd.append(random.choice(numbers))
        print("".join(pwd))

    if choose == 4:
        for i in range(int(length)):
            pwd.append(random.choice(allchars))
        print("".join(pwd))


if __name__ == "__main__":     
    choose()   
