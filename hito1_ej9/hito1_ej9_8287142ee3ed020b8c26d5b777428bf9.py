a = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c = float(input("Ingrese el término independiente de la primera ecuación: "))
d = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
e = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
f = float(input("Ingrese el término independiente de la segunda ecuación: "))

def resolver(a, b, c, d, e, f):
    determinante = a * e - b * d
    if determinante == 0:
        return None
    else:
        x = (c * e - b * f) / determinante
        y = (a * f - c * d) / determinante
        return x, y

# Resolver el sistema de ecuaciones
solucion = resolver(a, b, c, d, e, f)

# Imprimir las soluciones
if solucion is not None:
    x, y = solucion
    print("La solución del sistema de ecuaciones es:")
    print("x =", x)
    print("y =", y)
else:
    print("El sistema de ecuaciones no tiene solución única.")
