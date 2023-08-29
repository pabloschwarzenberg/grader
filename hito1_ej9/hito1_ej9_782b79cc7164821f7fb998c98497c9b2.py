x1=int(input('x1: '))
y1=int(input('y1: '))
n1=int(input('n1: '))
x2=int(input('x2: '))
y2=int(input('y2: '))
n2=int(input('n2: '))

import numpy as np

A = np.matrix([[x1,y1],[x2,y2]])

B = np.matrix([[n1],[n2]])

X = A**(-1)*B

print('El resultado de X es:', X)