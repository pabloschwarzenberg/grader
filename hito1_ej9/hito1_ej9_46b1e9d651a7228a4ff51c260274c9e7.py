#Sistema de Ecuaciones
 def resolver_sistema(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1
    if determinante ==  print("El sistema no tiene solución única.")
        return
    x = (c1 * b2 - c2 * b1) / determinante
    y = (a1 * c2 - a2 * c1) / determinante
    print(f"x = {round(x, 1)}")
    print(f"y = {round(y, 1)}")


# Pedir al usuario los coeficientes del sistema
a1 = float(input("Ingrese el coeficiente a1: "))
b1 = float(input("Ingrese el coeficiente b1: "))
c1 = float(input("Ingrese el coeficiente c1: "))

a2 = float(input("Ingrese el coeficiente a2: "))
b2 = float(input("Ingrese el coeficiente b2: "))
c2 = float(input("Ingrese el coeficiente c2: "))

# Llamar a la función para resolver el sistema
resolver_sistema(a1, b1, c1, a2, b2, c2)
     