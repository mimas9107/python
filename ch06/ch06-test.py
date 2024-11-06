# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 11:51:54 2024

@author: user
"""

array1=(11,33)
array2=(55,66)

print('tuple1:{0}, tuple2:{1}'.format(array1,array2))
print('串接: ', array1+array2)

array3 = 'abc','def'+ 'ghi','jkl'
print(array3)

print(array1 * 4)


ary=25, 63, 78, 92
for item in ary:
    print(item)
    
students =[['大雄',10,20,30],
           ['小夫',11,23,29],
           ['胖虎',99,199,299]]

for student in students:
    print(student)
    
for (name,a,b,c) in students:
    print(name, a, b,c)
    
    
data3 = ['Mary', [78,92], 'Eric', [65,91]]

for data in data3:
    if isinstance(data, str): 
        print(f"{data:>10}")
    else:
        for d in data:
            print(d, end=' ')
        print()
        
# 三維度陣列 2x3x2
mat3D =[ [[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]] ]

