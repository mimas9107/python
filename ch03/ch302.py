# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 13:58:01 2024

@author: user
"""
"""
設計一個程式, 使用者輸入購物金額,
並判斷如果購物金額1500(含)以上,才能享85折優惠,
程式最後會輸出需付款金額
(利用所學: input, eval, 運算, if)

"""

totalprice=int(input("購物金額= "))
if(totalprice>=1500): totalprice=totalprice*0.85
print(f"你需付款= {totalprice}")
