# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 08:51:46 2024

@author: justin

Chapter 02 exercise:

"""

num1,num2,num3 = eval(input("請輸入3個值, 用逗號隔開:"))
# step1 使用者 input輸入了 "10,20,30" 這個字串
# step2 這個字串餵給 eval()去執行這個字串, 然後 eval("10,20,30") 指定到 num1,num2,num3
# 相當於 num1,num2,num3=10,20,30 賦值

print(num1+num2+num3)