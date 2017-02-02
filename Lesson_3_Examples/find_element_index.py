#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 12:07:51 2016

@author: RashidKazmi
"""

# Define a procedure, find_element,
# using index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.

# If there is no matching element,
# return -1.
def find_element(p, t):
    if t in p:
        return p.index(t)
    else:
        return -1
   
def find_element1(p, t):
    if t not in p:
        return -1
    return p.index(t)
    
print (find_element1([1,2,3],3))
#>>> 2

print (find_element1(['alpha','beta'],'gamma'))
#>>> -1


