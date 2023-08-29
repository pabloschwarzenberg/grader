#Sistema de Ecuaciones
a1 = float(input("Ingrese el valor de x en la primera ecuación: "))
b1 = float(input("Ingrese el valor de y en la primera ecuación: "))
c1 = float(input("Ingrese el valor resultante en la primera ecuación: "))
a2 = float(input("Ingrese el valor de x en la segunda ecuación: "))
b2 = float(input("Ingrese el valor de y en la segunda ecuación: "))
c2 = float(input("Ingrese el valor resultante en la segunda ecuación: "))

denominador = a1 * b2 - a2 * b1
x = (b2 * c1 - b1 * c2) / denominador
y = (a1 * c2 - a2 * c1) / denominador

print("x =", round(x, 1))
print("y =", round(y, 1))
