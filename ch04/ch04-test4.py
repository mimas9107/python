# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 16:18:04 2024

@author: user
"""

import random
random.seed()

print(random.random())      # 0.0<= r <1

## 隨機挑選1個出來
ls=['john','marry','tom','jack']
print(random.choice(ls))

## 產生 1~100的亂數
print(random.randint(1,100)) # 1<= r <=100

## 產生10個亂數
for item in range(10):
    print(random.random())
    
## 打亂原始容器順序
random.shuffle(ls)
print(ls)