def resolver_sistema(a, b, c, d, e, f):
    determinante = a * e - b * d

    if determinante == 0:
        return None  # El sistema no tiene solución única
    else:
        x = (c * e - b * f) / determinante
        y = (a * f - c * d) / determinante
        return round(x, 1), round(y, 1)

# Solicitar al usuario los coeficientes del sistema
a = float(input("Ingrese el coeficiente 'a': "))
b = float(input("Ingrese el coeficiente 'b': "))
c = float(input("Ingrese el término independiente 'c': "))
d = float(input("Ingrese el coeficiente 'd': "))
e = float(input("Ingrese el coeficiente 'e': "))
f = float(input("Ingrese el término independiente 'f': "))

# Resolver el sistema de ecuaciones
soluciones = resolver_sistema(a, b, c, d, e, f)

# Imprimir las soluciones
if soluciones is None:
    print("El sistema no tiene solución única.")
else:
    x, y = soluciones
    print("Las soluciones son:")
    print("x =", x)
    print("y =", y)
