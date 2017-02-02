#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 14:51:59 2016

@author: RashidKazmi
"""
"""
if (year is not divisible by 4) then (it is a common year)
else if (year is not divisible by 100) then (it is a leap year)
else if (year is not divisible by 400) then (it is a common year)
else (it is a leap year)
"""

def leapYear(year):
    if(year % 400 == 0):
        return True
    if (year % 100 == 0):
        return True
    if (year % 4 == 0):
        return True
    return False

print (leapYear(2016))    