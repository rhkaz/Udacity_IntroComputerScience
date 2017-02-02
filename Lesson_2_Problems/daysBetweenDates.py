#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 12:55:21 2016

@author: RashidKazmi
"""

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30 :
        return year, month, day + 1
    else:
        if month < 10 :
            return year, month + 1, 1
        else:
            return year + 1, 1, 1
    
def dateIsBefore (year1, month1, day1, year2, month2, day2) :
    if year1 < year2 :
        return True
    if year1 == year2 :
        if month1 < month2 :
            return True
    else :
        if month1 == month2 :
            return day1 < day2
    return False
    
def daysBetweenDates (year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    assert not dateIsBefore (year2, month2, day2, year1, month1, day1)
    """assert to through error instead 0 - we will reverse order"""
    days = 0
    while dateIsBefore (year1, month1, day1, year2, month2, day2) :
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

print (daysBetweenDates(2013, 1, 24, 2013, 6, 29))
#print daysBetweenDates (2016, 1, 24, 2016, 6, 29)
#Sprint daysBetweenDates (1916, 1, 24,2016, 1, 24)
print (daysBetweenDates (2016, 1, 1, 2015, 12, 20))  
      

#def test():
#    test_cases = [((2012,9,30,2012,10,30),30), 
#                  ((2012,1,1,2013,1,1),360),
#                  ((2012,9,1,2012,9,4),3)]
#    
#    for (args, answer) in test_cases:
#        result = daysBetweenDates(*args)
#        if result != answer:
#            print "Test with data:", args, "failed"
#        else:
#            print "Test case passed!"
#
#test()
    