#!/usr/bin/python
aList = []
#Read user input and put them in a list
counter = 0
while counter < 5:
    userInput = input('Please input a number:')
    aList.append(int(userInput))
    counter += 1

#Count the numbers
listCount = 0
theSum = 0
while listCount < len(aList):
   theSum += aList[listCount] 
   listCount += 1
print('The sum is :', theSum)

