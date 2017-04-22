#!/usr/bin/env python

import fileinput 

def process(line):
    line2=line.lower()
    print(line2)    
 
for file in fileinput.input():
    process(file)