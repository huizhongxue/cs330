import numpy as np
import math

a = np.array([[1, 1, 1], [4, 2, 1], [9, 3, 1]])
b = np.array([1/np.e, np.power(2, 2.1)/np.power(np.e, 2), np.power(3, 2.1)/np.power(np.e, 3)])
x = np.linalg.solve(a, b)

print(x)