def resolver_un_sistema_de_ecuaciones(a, b, c, d, e, f):
    determinante = a * e - b * d
    if determinante != 0:
        x = (c * e - b * f) / determinante
        y = (a * f - c * d) / determinante
        return x, y
    else:
        return None

a = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c = float(input("Ingrese el resultado de la primera ecuación: "))
d = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
e = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
f = float(input("Ingrese el resultado de la segunda ecuación: "))

solucion = resolver_un_sistema_de_ecuaciones(a, b, c, d, e, f)

if solucion is not None:
    print(solucion)
else:
    print("El sistema de ecuaciones no tiene solución única.")