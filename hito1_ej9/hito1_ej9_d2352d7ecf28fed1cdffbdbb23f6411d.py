#Sistema de Ecuaciones
a=int(input())
b=int(input())
c=int(input())

d=int(input())
e=int(input())
f=int(input())

dis=a*e-b*d

x=((c*e-b*f)/dis)
y=((a*f-c*d)/dis)

print("x=",x)
print("y=",y)
