#!/usr/bin/env python
"""
a filter that split lines of text into word per line
"""
import fileinput
import re

def process(file):
    pattern =re.compile('\w+')
    file = pattern.findall(file)
    
    for i in file:
        if len(i)>=2:
            print(i)

  
for file in fileinput.input():
    process(file)
