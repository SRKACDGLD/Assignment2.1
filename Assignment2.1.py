# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 14:19:43 2018

@author: krishna.i


Assignment 2.1: Write a program which accepts a sequence of comma-separated
numbers from console and generate a list.
"""

mystr = input("ENTER Comma separated values: ")  # Accepting string input from the user

mylis1 = mystr.split(",")    # To split each word/number separated by comma "," from the given input string

mylis2 = []
for a in mylis1:        # iterating through each element in the list "mylis1"
    if a.lstrip().isnumeric():  # checking if an element in the list is numeric value
        mylis2.append(int(a.lstrip()))      # converting a numeric element to Number and appending in another list "mylis2"
    else:
        mylis2.append(a.lstrip())   # appending a character/string element without spaces in list "mylis2"

print(mylis2)  # Displaying MyLis2 elements 

# End of the code
