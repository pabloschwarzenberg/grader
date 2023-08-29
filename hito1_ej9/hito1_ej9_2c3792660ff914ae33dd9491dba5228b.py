#Sistema de Ecuaciones
a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())

discriminante=(a*e-d*b)

x2=(f*a-d*c)/discriminante
x1=(c-b*x2)/a
print("x=",round(x1,1),"y=",round(x2,1))