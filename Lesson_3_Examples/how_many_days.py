# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Given the variable,

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# define a procedure, how_many_days,
# that takes as input a number
# representing a month, and returns
# the number of days in that month.

def  how_many_days(month_number):
    # subtract -1 as elements of list starts from zero and 
    #month starts from 1
    num = days_in_month[month_number -1]
    return num
    
    
print (how_many_days(1))
#>>> 31

#print how_many_days(9)
#>>> 30
