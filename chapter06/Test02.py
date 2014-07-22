#!usr/bin/python
import keyword
import string

alphas = string.ascii_letters + '_'
numbers = string.digits
keywords = keyword.kwlist

userInput  = input('Please input a word:')
if userInput in keywords:
    print('The userInput: ' + userInput + '  is a keyword.')
else:
    if len(userInput) <= 1:
        print('''The Python identifier's length must > 1''')
    else:
        if userInput[0] not in alphas:
            print('invalid: First symbol must be alphabetic')
        else:
            for otherChar in userInput[1 : ]:
                if otherChar not in alphas + numbers:
                    print('invalid: Remaining symbols must be alphanumeric')
                    break
            else:
                print('It is ok')
