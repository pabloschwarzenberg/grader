#Sistema de Ecuaciones
import math
a=int(input("ingrese a:"))
b=int(input("ingrese b:"))
c=int(input("ingrese c:"))
d=int(input("ingrese d:"))
e=int(input("ingrese e:"))
f=int(input("ingrese f:"))
#ax+by=c
#dx+ey=f
#x=(c-by)/a
#d*((c-b*y)/a)+e*y=f
y=(f*a-d*c)/(-d*b+a*e)
x=(c-b*y)/a
print("x=",x)
print("y=",y)
