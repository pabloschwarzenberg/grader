#Sistema de Ecuaciones
a1 = float(input("Ingrese el valor de a1: "))
b1 = float(input("Ingrese el valor de b1: "))
c1 = float(input("Ingrese el valor de c1: "))
a2 = float(input("Ingrese el valor de a2: "))
b2 = float(input("Ingrese el valor de b2: "))
c2 = float(input("Ingrese el valor de c2: "))

x = (c1*b2-c2*b1)/(a1*b2-a2*b1)
y = (a1*c2-a2*c1)/(a1*b2-a2*b1)

print("'x=",round(x, 1),"'")
print("'y=",round(y, 1),"'")      