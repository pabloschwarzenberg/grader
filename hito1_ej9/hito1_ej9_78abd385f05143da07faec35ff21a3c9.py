#Sistema de Ecuaciones
A1 = float(input("Ingrese el primer valor de x de la primera ecuación: "))
B1 = float(input("Ingrese el primer valor de y de la primera ecuación: "))
C1 = float(input("Ingrese el valor al termino independiente de la primera ecuación: "))

A2= float(input("Ingrese el segundo valor de x de la segunda ecuación: "))
B2 = float(input("Ingrese el segundo valor de y de la segunda ecuación: "))
C2 = float(input("Ingrese el segundo valor independiente de la segunda ecuación: "))

# Calcular las soluciones del sistema
x = (C1*B2 - C2*B1) / (A1*B2 - A2*B1)
y = (A1*C2 - A2*C1) / (A1*B2 - A2*B1)

# Imprimir las soluciones redondeadas a un decimal
print("x =", round(x, 1))
print("y =", round(y, 1))      