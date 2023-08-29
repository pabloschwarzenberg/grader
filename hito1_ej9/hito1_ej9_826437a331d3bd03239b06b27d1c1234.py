#Sistema de Ecuaciones
x1 = int(input("Ingrese x1: "))
y1 = int(input("Ingrese y1: "))
c1 = int(input("Ingrese c1: "))
x2 = int(input("Ingrese x2: "))
y2 = int(input("Ingrese y2: "))
c2 = int(input("Ingrese c2: "))

y = ((c2*x1)-c1)/((y2*x1)-y1)
x = (c1-(y1*y))/x1
print("x=", round(x, 1))
print("y=", round(y, 1))      