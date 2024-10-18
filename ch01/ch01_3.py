# -*- coding: utf-8 -*-
"""
輸入輸出基本練習
print() 輸出結果到 stdio
input() stdio會提示訊息, 使用者輸入後, 輸入是字串!

"""
"""
Coding有3種錯誤
1. 邏輯上的錯誤
2. 執行期錯誤(runtime error)
3. 語法錯誤(syntax error; compilation-time error)

"""
print("Welcome to Python !","="*32,sep='\n')
try:
    age = input("Please your age : ")

    # 將輸入的 "字串" 轉成 "整數"型別, 存在 ages變數(整數)中,
    if("." not in age):
        ages = int(age)
    else:
        ages = float(age)
    
    # 判斷年齡是否大於等於20歲:
    if (ages>=20): 
        print("\nYou have right to vote !")
    else:
        print("\nYou don't have right to vote.")
        
except ValueError:
    print("OMG Please input your age in numbers")
    


