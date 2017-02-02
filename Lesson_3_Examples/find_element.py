#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 12:07:51 2016

@author: RashidKazmi
"""

# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element(qlist, value):
    count = 0
    for e in qlist:
        if e == value:
            return count
        count = count + 1
    return -1
   

print (find_element([1,2,3],3))
#>>> 2

print (find_element(['alpha','beta'],'gamma'))
#>>> -1


def find_element(p, t) :
    i = 0
    for e in p :
        if e == t :
            return i
        i = i + 1
    return -1