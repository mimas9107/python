# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 15:07:17 2024

閏年定義
1. 不可被4整除 平年
2. 可被4整除 且 不被100整除 閏年
3. 可被100整除 且 不被400整除 平年
4. 可被400整除 閏年


"""

def leapyear(year):
    # return (( year % 400 == 0) or (( year % 4 ==0) and (year % 100 !=0)))
    if( year % 4 != 0):
        return '平年'
    if( year % 4 == 0 ) and (year%100 != 0) :
        return '潤年'
    if( year % 100 == 0 ) and (year%400 != 0) :
        return '平年'
    if( year % 400 == 0):
        return '潤年'


year=int(input('year(in AD)= '))

print(f"{year} 是閏年嗎? {leapyear(year)}")

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def leapyear2(year):
    if (( year % 400 == 0) or (( year % 4 ==0) and (year % 100 !=0))):
        ##print('{} is leap year!'.format(year))
        ##print('yes')
        return 1
    else:
        ##print('no')
        return 0

a=0

##while (a != 'bye'):
##    a = input('input a year>>')
##    leapyear(int(a))
    
y = np.array(range(1000,2600))
##print(y)

yyy=[]
for yy in y:
    yesno=leapyear2(yy)
    if(yesno):
        yyy.append([yy,yesno])
print(yyy)