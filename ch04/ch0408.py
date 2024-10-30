# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 16:13:17 2024

@author: user
"""

total = 0
score = 0
count = 0

score = int(input("input score, or press 0 to quit>>"))
while(score != 0):
    total += score 
    count +=1
    score = int(input("input score, or press 0 to quit>>"))

average=float(total/count)
print(f"class= {total}, average= {average:8.2f}")