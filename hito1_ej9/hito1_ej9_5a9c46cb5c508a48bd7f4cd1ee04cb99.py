###Sistema de ecuaciones
import sys
import math

a=int(input('ingrese a: '))
b=int(input('ingrese b: '))
c=int(input('ingrese c: '))
d=int(input('ingrese d: '))
e=int(input('ingrese e: '))
f=int(input('ingrese f: '))

if a==0 or b==0 or d==0 or e==0:
    print('se ingresaron valores no validos')
    sys.exit(1)
    
discriminante=(a*e-d*b)

if discriminante==0:
    print('El sistema no se puede resolver.')
else:
    x2=(f*a-d*c)/discriminante
    x1=(c-b*x2)/a
    print('x = ',round(x1,1), ' ; y = ',round(x2,1), sep='')
