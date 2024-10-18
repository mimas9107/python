# -*- coding: utf-8 -*-
""" 多行註解
物聯網-AI程式設計與應用實務班
Python 程式語言 
Chapter 01 _1 
Hello world
"""
import color
str_prompts="Hello world!"
for e in range(10):
    o=e%3
    if(o==0):
        print(color.Colors.LIGHT_GREEN+str_prompts+color.Colors.END, end='')
    elif(o==1):
        print(color.Colors.LIGHT_RED+str_prompts+color.Colors.END, end='')
    else:
        print(color.Colors.LIGHT_BLUE+str_prompts+color.Colors.END, end='')

