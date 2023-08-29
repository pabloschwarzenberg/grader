#Sistema de Ecuaciones
def resolver_sistema(a, b, c, d, e, f):
    determinante = a * d - b * c
    if determinante == 0:
        return None

    x = (e * d - b * f) / determinante
    y = (a * f - c * e) / determinante

    return x, y

# Pedir los valores del sistema al usuario
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
d = float(input("Ingrese el valor de d: "))
e = float(input("Ingrese el valor de e: "))
f = float(input("Ingrese el valor de f: "))

# Resolver el sistema
soluciones = resolver_sistema(a, b, c, d, e, f)

# Imprimir las soluciones redondeadas a un decimal
if soluciones is None:
    print("El sistema no tiene solución única.")
else:
    x, y = soluciones
    print("x =", round(x, 1))
    print("y =", round(y, 1))
     