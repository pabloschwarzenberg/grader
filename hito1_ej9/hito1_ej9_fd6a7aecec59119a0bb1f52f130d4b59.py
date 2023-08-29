def resolver_sistema():
    print("Ingrese los coeficientes y las constantes del sistema de ecuaciones:")
    a1 = float(input("Coeficiente a1: "))
    b1 = float(input("Coeficiente b1: "))
    c1 = float(input("Constante c1: "))
    a2 = float(input("Coeficiente a2: "))
    b2 = float(input("Coeficiente b2: "))
    c2 = float(input("Constante c2: "))

    determinante = a1 * b2 - a2 * b1

    if determinante == 0:
        print("El sistema no tiene solución única.")
    else:
        x = (c1 * b2 - c2 * b1) / determinante
        y = (a1 * c2 - a2 * c1) / determinante
        print("x = (round(x, 1))")
        print("y = (round(y, 1))")

resolver_sistema()
        