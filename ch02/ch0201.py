# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 10:58:26 2024

@author: user
"""

num=123456789

# 捨去最低位數
num = num // 10 

# 取出最低位數
ls_digit = num % 10 

# ========(1)========
print("="*8 + "(1)" +"="*8)
num2 = 123456789
# get 5th digit from right.
num2 = num2 // 10 #123456789 -> 12345678
num2 = num2 // 10 #12345678 -> 1234567
num2 = num2 // 10 #1234567 -> 123456
num2 = num2 // 10 #123456 -> 12345
print("4 digits disposed ",num2)
ls_digit = num2 % 10
print("5th digit=",ls_digit)


# ========(2)========
print("="*8 + "(2)" +"="*8)

num3=123456789
print('initial num3=',num3)
print('transient= num3/10000=', num3/10000)

# num3=(num3//10000) % 10
num3=(num3//10**4) % 10
print("5th digit=",num3)