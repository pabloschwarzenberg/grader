from sympy import symbols, Eq, solve

# Obtener los coeficientes y términos independientes del sistema de ecuaciones
a1 = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c1 = float(input("Ingrese el término independiente en la primera ecuación: "))

a2 = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
c2 = float(input("Ingrese el término independiente en la segunda ecuación: "))

# Definir las variables simbólicas
x, y = symbols('x y')

# Definir las ecuaciones
ecuacion1 = Eq(a1*x + b1*y, c1)
ecuacion2 = Eq(a2*x + b2*y, c2)

# Resolver el sistema de ecuaciones
solucion = solve((ecuacion1, ecuacion2), (x, y))

# Imprimir las soluciones redondeadas a un decimal
print("x =", round(solucion[x], 1))
print("y =", round(solucion[y], 1))

