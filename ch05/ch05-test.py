# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 09:05:29 2024

@author: user
"""

mystring='ppythonn'

for i in mystring:
    print(i,end='')
print()
print("="*8)
for idx,item in enumerate(mystring):
    print(idx, "==>", item)

print("="*8)
for idx,item in enumerate(mystring,start=2):
    print(idx, "==>", item)
    
words="Hello python is very popular!"
print(words[5:])
print(words[6:13])