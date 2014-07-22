#!/usr/bin/python
# put numbers into a list
aList = []
for c in range(5):
    userInput = input('Please input a number:')
    aList.append(int(userInput))

# count the sum of numbers in list
sum = 0
for d in range(len(aList)):
    sum += aList[d]
print('The sum is :', sum)
