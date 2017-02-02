#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 13:12:54 2016

@author: RashidKazmi
"""
# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.

def split_string(source,splitlist):
    words_list = []
    atsplit = True
    for char in source :
        if char in splitlist:
            atsplit = True 
        else: 
            if atsplit :
                words_list.append(char)
                atsplit = False
            else:
                words_list[-1] = words_list[-1] + char
    return words_list 

out = split_string("This is a test-of the,string separation-code!"," ,!-")
print (out)

#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

#out = split_string("After  the flood   ...  all the colors came out.", " .")
#print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

#out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
#print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']