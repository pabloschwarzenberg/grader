#Sistema de Ecuaciones
import numpy as np
a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())


x= np.array([ [a,b], [d,e] ])
z= np.array([c,f])
l= np.linalg.solve(x,z)
print("x="+str(round(float(l[0]), 1)))
print("y="+str(round(float(l[1]), 1)))
