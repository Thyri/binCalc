"""
binCalc.py
Authord by Max Maurin
created 12/20/2013
"""

from math import *


"""
purpose: to find to what power of 2 is just greater than myInt
pre: cursor = 0, myInt is of type int
returns: cursor -> an int representative of a power to which 2 is raised that is greater than myInt
"""
def d2bCursor(myInt, cursor):
    if myInt > pow(2, cursor):
        return d2bCursor(myInt, cursor+1) #incrememnts the power of 2 up only until 2 to the power of cursor is greater than myInt
    else:
        return cursor

"""
purpose:to create a string of 0's and 1's based on comparison between myInt and cursor
pre: cursor is greater than or equal to 0
returns: myString -> the final binary value. not including the head, which will always be 0
"""
def d2bCalc(myInt, cursor, myString):
    if cursor >= 0:
        if myInt > pow(2,cursor):
            d2bCalc(myInt - pow(2,cursor), cursor -1 ,myString + '1') #if cursor can be subtracted from myInt, it is, and cursor is less one. the string appended a 1
        else:
            d2bCalc(myInt , cursor -1 ,myString + '0') #if the cursor can not be subracted from myInt, cursor is less one and myString is appended a 0
    else:
        print(myString[1:]) # prints all but the head of myString, as by using the first value of 2^cursor as the first value greater than myInt, myString[0] will always be 0

def main():
    print('-------------------------------------------------')
    myInt = int(input("Input the integer you want converted please. "))+1
    cursor = d2bCursor(myInt, 0)
    print("The base 2 form of ", myInt - 1, " is:")
    d2bCalc(myInt, cursor, '')
    print('-------------------------------------------------')
            
main()
