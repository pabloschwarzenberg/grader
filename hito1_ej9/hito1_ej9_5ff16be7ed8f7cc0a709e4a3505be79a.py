def resolver_sistema(a, b, c, d, e, f):
    determinante = a * d - b * c

    if determinante == 0:
        return None

    x = (e * d - b * f) / determinante
    y = (a * f - c * e) / determinante

    return x, y


# Solicitar al usuario los coeficientes del sistema de ecuaciones
a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))
d = float(input("Ingrese el coeficiente d: "))
e = float(input("Ingrese el coeficiente e: "))
f = float(input("Ingrese el coeficiente f: "))

# Resolver el sistema de ecuaciones
soluciones = resolver_sistema(a, b, c, d, e, f)

# Imprimir las soluciones redondeadas a un decimal
if soluciones is not None:
    x, y = soluciones
    print(f"x = {round(x, 1)}")
    print(f"y = {round(y, 1)}")
else:
    print("El sistema de ecuaciones no tiene solución única.")
9
7