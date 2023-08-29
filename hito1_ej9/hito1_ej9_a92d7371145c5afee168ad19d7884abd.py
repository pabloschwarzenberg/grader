#Sistema de Ecuaciones
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())

x=round((e*c-b*f)/(a*e-d*b),1)
y=round((a*f-d*c)/(a*e-d*b),1)

print("x=",x)
print("y=",y)
