# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 15:38:51 2024

@author: user
"""

score = int(input("score:"))

if(score<60): #0~59
    print("F")
elif(score<63): #60~62
    print("C-")
elif(score<67): #63~66
    print("C")
elif(score<70): #67~69
    print("C+")
elif(score<73): #70~72
    print("B-")
elif(score<77): #73~76
    print("B")
elif(score<80): #77~79
    print("B+")
elif(score<85): #80~84
    print("A-")
elif(score<89): #85~90
    print("A")
else:           #100~90
    print("A+")
    



match score:
    case score if score<60:
        print("F")
    case score if score<63:
        print("C-")
    case _:
        print("other")
        
            
        