#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 14:35:18 2016

@author: RashidKazmi
"""

# Define a procedure, add_page_to_index,
# that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

# It should update the index to include
# all of the word occurences found in the
# page content by adding the url to the
# word's associated url list.

index = []
def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return 
    index.append([keyword,[url]])
      
def add_page_to_index(index,url,content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

        
add_page_to_index(index,'fake.text',"This is a test")
print (index)
#>>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
#>>> ['test',['fake.text']]]
   
    
add_page_to_index(index, 'http://randy.pausch',
                  """
                  Good judgment comes from experience, experience comes from 
                  bad judgment. If things aren't going well it probably you are 
                  learning a lot and things will go better later.
                  ----- Randy Pausch
                  """)
print (index)             
                  
                  
        













































