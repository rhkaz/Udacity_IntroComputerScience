#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 12:43:06 2016

@author: RashidKazmi
"""
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
