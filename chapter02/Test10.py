#!/usr/bin/python
userInput = input('Please input a number:')
try:
    inputNumber = int(userInput)
    if inputNumber < 100 and inputNumber > 0:
        print('success')
    else:
        input('Please input a number:')
except Exception:
    input('Please input a number:')
