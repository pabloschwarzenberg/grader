#Sistema de Ecuaciones
import numpy as np
a=np.array([[2,3],[1,2]])
b=np.array([6,5])
x=np.linalg.solve(a,b)
print(x)