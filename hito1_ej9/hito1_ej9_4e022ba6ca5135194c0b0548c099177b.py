#Sistema de Ecuaciones
from sympy import symbols, Eq, solve

# Definir las incógnitas
x, y = symbols('x y')

# Pedir los coeficientes del sistema de ecuaciones
a1 = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c1 = float(input("Ingrese el término independiente de la primera ecuación: "))

a2 = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
c2 = float(input("Ingrese el término independiente de la segunda ecuación: "))

# Definir las ecuaciones
ecuacion1 = Eq(a1 * x + b1 * y, c1)
ecuacion2 = Eq(a2 * x + b2 * y, c2)

# Resolver el sistema de ecuaciones
solucion = solve((ecuacion1, ecuacion2), (x, y))

# Imprimir las soluciones redondeadas a un decimal
print(f"x = {solucion[x]:.1f}")
print(f"y = {solucion[y]:.1f}")

