# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 14:33:40 2024

@author: user
"""

def digitsum(num):
    total=0
    rem=0
    while num>0:
        rem = num%10
        total+=rem
        num //=10
    if (total // 10 !=0 ):
        return digitsum(total)
    else:
        return total
    

num=123456
total=0

while num>0:
    remain = num%10
    total+=remain
    num //=10
    print(f"{num:6d} {remain:8d} {total:7d}")

print("remain =>", total)

print(digitsum(123456))

