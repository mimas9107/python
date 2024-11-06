# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:35:35 2024

@author: user
"""




area = ['北','南']
city = ['左營','楠梓','鳳山']
## 一般 for-loop:
result = []
for one in area:
    if one != '南':
        for two in city:
            if two != '鳳山':
                result.append(one+two)
print(result)

## 串列生成式:
comb2 = [ a + c for a in area for c in city if(a != '南' and c != '鳳山')]

print(comb2)


## ==== 我自己比較一下傳統迴圈 跟串列生成式執行時間 ====
a=[n for n in range(1,1000000)]

import time
start1=time.time()
t=0
for e in a:
    t+=e
stop1=time.time()
print("for-loop: Elasped time=",stop1-start1)

start2=time.time()

res=sum([t for t in a])
stop2=time.time()
print("List comprehension: Elasped time=",stop2-start2)

print("t=",t)
print("res=",res)