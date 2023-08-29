#Sistema de Ecuaciones
# Obtener los coeficientes y constantes del sistema de ecuaciones
a1 = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c1 = float(input("Ingrese la constante en la primera ecuación: "))

a2 = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
c2 = float(input("Ingrese la constante en la segunda ecuación: "))

determinante = a1 * b2 - a2 * b1
solucion_x = (c1 * b2 - c2 * b1) / determinante
solucion_y = (a1 * c2 - a2 * c1) / determinante

# Imprimir soluciones redondeadas
print("x =", round(solucion_x, 1))
print("y =", round(solucion_y, 1))