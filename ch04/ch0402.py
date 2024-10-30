# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 09:41:42 2024

@author: user
"""


##==== 乘法表 負數擴展版 XD ====
print("="*8, "整數乘法表","="*8)
lower=int(input("請輸入整數下限>> "))
upper=int(input("請輸入整數上限>> "))

print(" "*2,"|",sep='',end='')
for k in range(lower,upper+1):
    print(f"{k:3d}",end='') #表格 column header
print("\n")
print("-"*(upper-lower+2)*3) #表格上格線

for i in range(lower,upper+1):
    print(f"{i:2d}", "|",sep='', end='') # 表格 row header
    for j in range(lower,upper+1):
        print(f"\033[1;33m{i*j:3d}\033[0m",sep='',end='') # 內容
    print("\n")
    
