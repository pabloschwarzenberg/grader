# Sistema de Ecuaciones
# Resolución de un sistema de ecuaciones lineales
# con dos incógnitas

# Ingresar los coeficientes y constantes del sistema
a1 = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c1 = float(input("Ingrese la constante en la primera ecuación: "))

a2 = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
c2 = float(input("Ingrese la constante en la segunda ecuación: "))

# Calcular la determinante del sistema
determinante = a1 * b2 - a2 * b1

# Verificar si el sistema tiene solución única
if determinante == 0:
    print("El sistema no tiene solución única.")
else:
    # Calcular las soluciones
    x = (c1 * b2 - c2 * b1) / determinante
    y = (a1 * c2 - a2 * c1) / determinante

    # Imprimir las soluciones redondeadas a un decimal
    print("x =", round(x, 1))
    print("y =", round(y, 1))