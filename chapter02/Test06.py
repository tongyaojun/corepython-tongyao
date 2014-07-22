#!/usr/bin/python
userInput = input('Please input a number:')
inputNum = int(userInput)
if inputNum > 0:
    print('Your number is a positive number')
elif inputNum < 0:
    print('Your number is a negative number')
else:
    print('Your number is zero')
