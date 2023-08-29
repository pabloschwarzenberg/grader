#Sistema de Ecuaciones
# Obtener los coeficientes y constantes del sistema
a1 = float(input("Ingrese el coeficiente de x de la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente de y de la primera ecuación: "))
c1 = float(input("Ingrese la constante de la primera ecuación: "))

a2 = float(input("Ingrese el coeficiente de x de la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente de y de la segunda ecuación: "))
c2 = float(input("Ingrese la constante de la segunda ecuación: "))

# Calcular las soluciones del sistema
determinante = a1 * b2 - a2 * b1

if determinante == 0:
    print("El sistema no tiene solución única.")
else:
    x = (c1 * b2 - c2 * b1) / determinante
    y = (a1 * c2 - a2 * c1) / determinante

    # Imprimir las soluciones redondeadas a un decimal
    print("x =", round(x, 1))
    print("y =", round(y, 1))
      