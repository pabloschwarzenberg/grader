#Sistema de Ecuaciones
a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())

x=float(((c-(b*f/e))/(a-b*d/e)))
y=float((f-(d*x))/e)
print("x=",x)
print("y=",y)