#Sistema de Ecuaciones
a=int(input("Ingrese primer valor:"))
b=int(input("Ingrese segundo valor:"))
c=int(input("Ingrese tercer valor:"))
d=int(input("Ingrese cuarto valor:"))
e=int(input("Ingrese quinto valor:"))
f=int(input("Ingrese sexto valor:"))

discriminante= a*e - b*d

while discriminante != 0:
    x=(c*e - b*f) / discriminante
    y=(a*f - c*d) / discriminante
    break

print("x=",x)
print("y=",y)
      