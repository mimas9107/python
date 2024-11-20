# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:09:10 2024

@author: user
"""

## 一般 for-loop寫法:
numA=[]
for i in range(10,31):
    numA.append(i)
print(numA)

print()

## 串列生成式:
numB = [i for i in range(10,31)]
print(numB) # 一行打完收工