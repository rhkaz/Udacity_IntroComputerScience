#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 10:06:58 2016

@author: RashidKazmi
"""
# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list_of_numbers):
    big = 0
    for  e in list_of_numbers:
        if (e > big):
            big = e
    return big


print (greatest([4,23,1]))
#>>> 23
#print (greatest([]))
#>>> 0

