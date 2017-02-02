#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 15:03:39 2016

@author: RashidKazmi
"""
def ifIsLeapYear(year):
    if(year % 400 == 0):
        return True
    if (year % 100 == 0):
        return True
    if (year % 4 == 0):
        return True
    return False
    
def daysInMonth(year, month): 
    if month == 1 or month == 3 or month == 5 or month ==7 \
    or month == 8 or month == 10 or month == 12:
        return 31
    else:
        if month == 2 :
            if ifIsLeapYear (year):
                return 29
            return 28
        else:
            return 30

print (daysInMonth(2016, 12))