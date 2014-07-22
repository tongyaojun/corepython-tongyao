#!/usr/bin/python
#sort input numbers
userInput1 = int(input('Please input a number:'))
userInput2 = int(input('Please input a number:'))
userInput3 = int(input('Please input a number:'))

def getBiggerNum(num1, num2):
    if num1 > num2:
        return num1
    else :
        return num2

biggerNum = getBiggerNum(userInput1, userInput2)
biggestNum = getBiggerNum(biggerNum, userInput3)
print('The biggest num is:', biggestNum)
