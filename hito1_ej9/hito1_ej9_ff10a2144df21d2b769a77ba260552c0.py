#Sistema de Ecuaciones
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())

y=(f*a-d*c)/(a*e-d*b)
x=(c-y*b)/a

print("x=",round(x,1),"y=",round(y,1))