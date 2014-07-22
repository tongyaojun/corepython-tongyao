#!user/bin/python
#loop 'for' test
userInput = input('Please input a word:')
for c in userInput:
    print(c)
userInput2 = input('Please input a word again:')
for d in range(len(userInput2)):
    print(userInput2[d])
