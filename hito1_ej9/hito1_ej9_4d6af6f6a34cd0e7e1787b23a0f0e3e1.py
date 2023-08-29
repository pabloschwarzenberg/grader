#Sistema de Ecuaciones
print("Ingrese valores ecuación 1")
a1=int(input("Ingrese a1: "))
b1=int(input("Ingrese b1: "))
c1=int(input("Ingrese c1: "))


print("Ingrese valores ecuación 2")
a2=int(input("Ingrese x2: "))
b2=int(input("Ingrese y2: "))
c2=int(input("Ingrese c2: "))

d=int(a1*b2-a2*b1)
dx=int(c1*b2-c2*b1)
dy=int(a1*c2-a2*c1)

x=(dx/d)
y=(dy/d)

print("x=",x)
print("y=",y)
