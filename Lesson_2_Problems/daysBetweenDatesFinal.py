#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 15:09:16 2016

@author: RashidKazmi
"""
# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def ifIsLeapYear(year):
    if(year % 400 == 0):
        return True
    if (year % 100 == 0):
        return True
    if (year % 4 == 0):
        return True
    return False

#ifIsLeapYear (2000)
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


def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if (day < 30):
        return year, month, day + 1
    if (year < 12):
        return year, month + 1, 1
    else:
        return year + 1, 1, 1


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2.
    Otherwise, returns False."""    
    if (year1 < year2):
        return True
    if (year1 == year2):
        return month1 < month2
    if (month1 == month2):
        return day1 < day2
    return False

    
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
       # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days
       
       
# test with 30 days
def mytest():
    assert daysBetweenDates(2013, 1, 1, 2013, 1,1) ==  0
    assert daysBetweenDates(2013, 1, 1, 2013, 1,2) ==  1
    assert nextDay(2013, 1, 1) ==  (2013, 1, 2)
    assert nextDay(2013, 4, 30) == (2013, 5, 1)
    assert nextDay(2012, 12, 31) ==  (2013, 1, 1)
    assert nextDay(2013, 9, 30) == (2013, 10, 1)
    assert daysBetweenDates (2013, 1, 1, 2014, 1, 1) == 365
    assert daysBetweenDates (2012, 1, 1, 2013, 1, 1) == 366
    assert daysBetweenDates (2013, 1, 24, 2013, 6, 29) == 156
    print ("Tests finished !!")
mytest ()

# def test():
#     test_cases = [((2012,1,1,2012,2,28), 58),
#                   ((2012,1,1,2012,3,1), 60),
#                   ((2011,6,30,2012,6,30), 366),
#                   ((2011,1,1,2012,8,8), 585 ),
#                   ((1900,1,1,1999,12,31), 36523)]
#
#     for (args, answer) in test_cases:
#         result = daysBetweenDates(*args)
#         if result != answer:
#             print "Test with data:", args, "failed"
#         else:
#             print "Test case passed!"
#
# test()