# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:08:27 2024

@author: user
"""

mymoney = 50000
rate = 2.0

target = 2* mymoney

year=0

while mymoney<target:
    year+=1
    interest=mymoney*(rate/100)
    mymoney+=interest
    
    print(f"{year} year - 存款={mymoney:8.1f} ")

print("year=", year)