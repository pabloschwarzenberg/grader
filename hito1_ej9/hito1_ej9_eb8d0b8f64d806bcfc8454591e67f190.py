#Sistema de Ecuaciones
print("Según el sistema de ecuaciones a*x+b*y=c y d*x+e*y=f")
a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())
y=(d*c-a*f)/(-a*e+d*b)
x=(c-b*y)/a
print("Entonces")
print (("x="), round(x,1))
print (("y="), round(y,1))
      