#!/usr/bin/env python

import fileinput
import re

def process(line):
    stopword=['and','the','to','of','her','it','in','you','she','for']
    pattern=re.compile('\w+')
    file=pattern.findall(line)
    

    for i in file:
        if i not in stopword:
            print(i)
 
    

 
for file in fileinput.input():
    process(file)