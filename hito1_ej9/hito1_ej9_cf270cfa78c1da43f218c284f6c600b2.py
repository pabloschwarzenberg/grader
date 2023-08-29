def resolver_sistema(a, b, c, d, e, f):
    determinante = a * d - b * c
    
    if determinante != 0:
        x = (e * d - b * f) / determinante
        y = (a * f - c * e) / determinante
        return round(x, 1), round(y, 1)
    else:
        return None

# Ejemplo de uso
a = float(input("Ingrese el coeficiente 'a' de la primera ecuación: "))
b = float(input("Ingrese el coeficiente 'b' de la primera ecuación: "))
c = float(input("Ingrese el término independiente 'c' de la primera ecuación: "))

d = float(input("Ingrese el coeficiente 'a' de la segunda ecuación: "))
e = float(input("Ingrese el coeficiente 'b' de la segunda ecuación: "))
f = float(input("Ingrese el término independiente 'c' de la segunda ecuación: "))

solucion = resolver_sistema(a, b, c, d, e, f)

if solucion:
    x, y = solucion
    print(f"x = {x}")
    print(f"y = {y}")
else:
    print("El sistema no tiene solución única.")

