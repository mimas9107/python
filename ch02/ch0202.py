# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 11:37:38 2024

@author: user
"""



"""
# ax^2+bx+c=0
a=2
b=7
c=1
#
find the roots=?
"""

#import math

# coeffients of the quodratic equation:
a,b,c=2,7,1

det = (b**2-4*a*c)**0.5
x1 = (-b+(det))/(2*a)
x2 = (-b-(det))/(2*a)

print("coeffients of the quodratic equation (a,b,c)= ", a,b,c)
print("root1= ", x1)
print("root2= ", x2)


# ==========================================================================
# ==== Plot the figure to verify the roots ====
import numpy as np
import matplotlib.pyplot as plt


x=np.array(list(range(-500,100)))/100
y=a*x**2+b*x+c
y2=np.array([0 for i in range(-500,100)])/100
plt.plot(x,y,'-',x,y2,'-')

plt.show()
