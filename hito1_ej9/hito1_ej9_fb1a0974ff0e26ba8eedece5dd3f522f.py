#Sistema de Ecuaciones
a1=int(input("A1:"))
b1=int(input("B1:"))
c1=int(input("C1:"))
a2=int(input("A2:"))
b2=int(input("B2:"))
c2=int(input("C2:"))

detp = float(a1*b2 - a2*b1)
detx = float(c1*b2 - c2*b1)
dety = float(a1*c2 - a2*c1)

print(detp)
print(detx)
print(dety)

x = detx/detp
y = dety/detp

print("x=",x)
print("y=",y)
