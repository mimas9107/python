# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 08:30:04 2024

@author: user
"""

import random

# 1. 講義版
num=random.randint(1,100)
guess=-1
while(True):
    guess=int(input('Please guess a number between 1 and 100: '))
    if (guess == num):
        print('Right! The answer is:', num)
        break;
    elif guess>=num:
        print(' number is too big')
    else:
        print(' number is too small')
        
        
# 2. 老師改進版

number = random.randint(1, 100)
guess =-1

while(guess != number):
    guess=int(input('Please guess a number between 1 and 100: '))
    if(guess >= number):
        print(' number is too big')
    else:
        print(' number is too small')

print(' Right guess! The answer is:', number)