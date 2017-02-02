#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 14:25:18 2016

@author: RashidKazmi
"""

# Define a procedure, lookup,
# that takes two inputs:

# - an index
# - keyword

# The procedure should return a list
# of the urls associated
# with the keyword. If the keyword
# is not in the index, the procedure
# should return an empty list.

index = [['udacity', ['http://udacity.com', 'http://npr.org']],
         ['computing', ['http://acm.org']]]
         
def lookup(index, keyword):
    for entry in index:
        if (entry[0] == keyword):
            return entry[1]
    return []
            
         
         
         
print (lookup(index,'udacity'))
#>>> ['http://udacity.com','http://npr.org']