#Sistema de Ecuaciones
a1 = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c1 = float(input("Ingrese el término independiente de la primera ecuación: "))

a2 = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
c2 = float(input("Ingrese el término independiente de la segunda ecuación: "))

# Calcular las soluciones del sistema
determinante = a1 * b2 - a2 * b1

if determinante == 0:
    print("El sistema no tiene solución única.")
else:
    x = (c1 * b2 - c2 * b1) / determinante
    y = (a1 * c2 - a2 * c1) / determinante

    # Imprimir las soluciones redondeadas a un decimal
    print("Las soluciones del sistema son:")
    print("x =", round(x, 1))
    print("y =", round(y, 1))