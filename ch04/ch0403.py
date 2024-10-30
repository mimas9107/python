# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 10:34:05 2024

@author: user
"""
# ==== solution 1 ====
for i in range(1,10):
    for j in range(1,i+1):
        print("*",end='')
    print()

for i in range(10,19):
    for j in range(18-i+1,0,-1):
        print("*",end='')
    print()


# ==== solution 2 ====
for i in range(1,19): # i=1~18
    print("*"*(i if i<10 else 18-i+1))
    
# ==== solution 2等效 ====
for i in range(1,19):
    if i<10:
        for j in range(i):
            print("*",end='')
        print()
    else:
        for j in range(19-i):
            print("*",end='')
        print()
        