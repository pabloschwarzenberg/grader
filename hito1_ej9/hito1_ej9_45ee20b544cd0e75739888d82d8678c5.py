#Sistema de Ecuaciones
# Entrada de los coeficientes y términos independientes
a1 = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c1 = float(input("Ingrese el término independiente de la primera ecuación: "))
a2 = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
c2 = float(input("Ingrese el término independiente de la segunda ecuación: "))

# Cálculo de las soluciones
denominador = a1 * b2 - a2 * b1

if denominador == 0:
    print("El sistema no tiene solución única.")
else:
    x = (b2 * c1 - b1 * c2) / denominador
    y = (a1 * c2 - a2 * c1) / denominador

    # Impresión de las soluciones redondeadas a un decimal
    print("x =", round(x, 1))
    print("y =", round(y, 1))