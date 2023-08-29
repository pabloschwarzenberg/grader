#Sistema de Ecuaciones
def resolver_sistema():
    print("Ingrese los coeficientes de la primera ecuación:")
    a1 = float(input("Coeficiente de x: "))
    b1 = float(input("Coeficiente de y: "))
    c1 = float(input("Término independiente: "))

    print("Ingrese los coeficientes de la segunda ecuación:")
    a2 = float(input("Coeficiente de x: "))
    b2 = float(input("Coeficiente de y: "))
    c2 = float(input("Término independiente: "))

    determinante = a1 * b2 - a2 * b1

    if determinante == 0:
        # El sistema no tiene solución única
        print("El sistema no tiene solución única.")
    else:
        x = (c1 * b2 - c2 * b1) / determinante
        y = (a1 * c2 - a2 * c1) / determinante
        print(f"x = {round(x, 1)}")
        print(f"y = {round(y, 1)}")


# Ejecutar la función para resolver el sistema
resolver_sistema()
