#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 09:16:23 2016

@author: RashidKazmi
"""
# Define a procedure, udacify, that takes as
# input a string, and returns a string that
# is an uppercase 'U' followed by the input string.
# for example, when you enter

# print udacify('dacians')

# the output should be the string 'Udacians'

def udacify(s):
    return 'U' + s

"""def udacity(s):
    s = 'U' + s[:]
    return s"""


# Remove the hash, #, from infront of print to test your code.

print (udacify('dacians'))
#>>> Udacians

print (udacify('turn'))
#>>> Uturn

print (udacify('boat'))
#>>> Uboat






