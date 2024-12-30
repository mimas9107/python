import numpy as np

x = [1, 2, 3, 4]
y = [4, 3, 2, 1]
z = x + y
print('python array/list:')
print('z = ', z)
print(type(z))

x = np.array([1, 2, 3, 4])
y = np.array([4, 3, 2, 1])
z = x + y
print('numpy array/list:')
print('z = ', z)
print(type(z))
