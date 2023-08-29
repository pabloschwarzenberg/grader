#Sistema de Ecuaciones
 
x1 = int(input("Ingrese x1: "))
y1 = int(input("Ingrese y1: "))
n1 = int(input("Ingrese n1: "))
x2 = int(input("Ingrese x2: "))
y2 = int(input("Ingrese y2: "))
n2 = int(input("Ingrese n2: "))

y = round((n1 - x1*n2)/(y1*x2 - x1*y2),1)
x = round((n1 - y1*y) / x1, 1)

print("x =", end="")
print(x)
print("y =", end="")
print(y)