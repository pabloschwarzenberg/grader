#Sistema de Ecuaciones
print("Resolvamos un sistema de ecuaciones de la forma ax+by=c, dx+ey=f")
a=float(input("a= "))
b=float(input("b= "))
c=float(input("c= "))
d=float(input("d= "))
e=float(input("e= "))
f=float(input("f= "))

y=(d*c-a*f)/(d*b-a*e)
x=(e*c-b*f)/(e*a-b*d)

print("x=",x)
print("y=",y)     