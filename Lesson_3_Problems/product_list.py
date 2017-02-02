#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 09:56:37 2016

@author: RashidKazmi
"""

# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

# def product_list(list_of_numbers):
def product_list(list_of_numbers):
    total = 1 #critical step works for all list
    for i in list_of_numbers:
        total= total * i # this will ensure that each elements are multiplied by itself
    return total
        


print (product_list([9]))
#>>> 9

print (product_list([1,2,3,4]))
#>>> 24

print (product_list([]))
#>>> 1