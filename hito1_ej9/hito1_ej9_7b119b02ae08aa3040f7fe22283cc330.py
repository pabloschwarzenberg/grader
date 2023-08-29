#Sistema de Ecuaciones
import math

# Pedimos los valores de las ecuaciones
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
d = float(input("Ingrese el valor de d: "))
e = float(input("Ingrese el valor de e: "))
f = float(input("Ingrese el valor de f: "))

# Realizamos las operaciones necesarias para obtener las soluciones
x1 = (d*e - b*f) / (a*e - b*d)
y1 = (a*f - c*e) / (a*e - b*d)
x2 = (c*d - a*f) / (a*d - c*b)
y2 = (a*f - c*d) / (a*d - c*b)

# Redondeamos las soluciones a dos decimales
x1 = round(x1, 2)
y1 = round(y1, 2)
x2 = round(x2, 2)
y2 = round(y2, 2)

# Imprimimos las soluciones
print("Solución 1: x =", x1, "y =", y1)
print("Solución 2: x =", x2, "y =", y2)