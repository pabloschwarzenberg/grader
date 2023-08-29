#Sistema de Ecuaciones
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())

a1=c*e-b*f
a2=a*e-b*d
a3=a*f-c*d

x=a1/a2
y=a3/a2

print("x=",x,"y=",y)