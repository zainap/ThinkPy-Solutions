# Modify the program to fix this error.

# Current Status: Complete

prefixes = 'JKLMNOPQ'
suffix = 'ack'

def ducks():
    for i in prefixes:
        if i == "O" or i == "Q":
            print (i + "u" + suffix)
        else:
            print (i + suffix)

ducks()
