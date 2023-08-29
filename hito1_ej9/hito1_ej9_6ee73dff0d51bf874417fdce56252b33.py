#Sistema de Ecuaciones
import sys
import math

print("Asigne valores a las constantes")
a=int(input("valor de a: "))
b=int(input("valor de b: "))
c=int(input("valor de c: "))
d=int(input("valor de d: "))
e=int(input("valor de e: "))
f=int(input("valor de f: "))

if a==0 or b==0 or d==0 or e==0:
    print("valores no validos")
    sys.exit(1)

delta=(a*e-d*b)

if(delta==0):
    print("No se puede resolver")
else:
    x2=(f*a-d*c)/delta
    x1=(c-b*x2)/a
    print("x=", round(x1,1),"y=", round(x2,1))

