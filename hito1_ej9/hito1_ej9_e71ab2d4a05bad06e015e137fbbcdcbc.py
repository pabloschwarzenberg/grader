#Sistema de Ecuaciones
      # Obtener los coeficientes y constantes del sistema de ecuaciones
a1 = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c1 = float(input("Ingrese la constante en la primera ecuación: "))

a2 = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
c2 = float(input("Ingrese la constante en la segunda ecuación: "))

# Calcular las soluciones del sistema de ecuaciones
determinante = a1 * b2 - a2 * b1

if determinante != 0:
    x = (c1 * b2 - c2 * b1) / determinante
    y = (a1 * c2 - a2 * c1) / determinante
    print(f"x = {round(x, 1)}")
    print(f"y = {round(y, 1)}")
else:
    print("El sistema de ecuaciones no tiene solución única.")
