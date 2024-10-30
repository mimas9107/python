# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:20:55 2024

乘法表全用 while改寫
"""

header=1
print("  |", end='')
while header<10:
    print(f"{header:3d}", end='')
    header+=1
print()

bar=1
while bar<31:
    print("-",end='')
    bar+=1
print()

i=1
while i<10:
    print(f"{i:2d}|", end='')
    j=1
    while j<10:
       print(f"{i*j:3d}",end='')
       j+=1;
    print()
    i+=1
    