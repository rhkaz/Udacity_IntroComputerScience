#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 10:23:10 2016

@author: RashidKazmi
"""
# Define a procedure, countdown, that takes a
# positive whole number as its input, and prints
# out a countdown from that number to 1,
# followed by Blastoff!
# The procedure should not return anything.
# For this question, you just need to call 
# the procedure using the line
# countdown(3)
# instead of print countdown(3).

def countdown(num):
    while (num > 0):
        print (num)
        num = num - 1
    print ('Blastoff')
   
   
countdown(3)
#>>> 3
#>>> 2
#>>> 1
#>>> Blastoff!
