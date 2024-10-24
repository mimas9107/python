# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 13:41:16 2024

@author: user
"""

score = int(input('please input score:'))

# isPass=score>=60
if score >= 60:
    # f"str{}" <== f字串, 裏頭用 {variable} 格式化字串
    print(f"你的分數{score}, pass..")
else:
    print("沒過, 拍拍...")

num=score
# 檢查 2的倍數 and 3的倍數
res=(num%2==0) and (num%3==0)
print(num, "是否為 2及3的倍數",res)