def solucion_sistema_ecuaciones(a, b, c, d, e, f):
    determinante = a*e - b*d
    if determinante != 0:
        x = (c*e - b*f) / determinante
        y = (a*f - c*d) / determinante
        return x, y
    else:
        return None, None
print("ingresa valores: ")
a, b, c, d, e, f = map(float, input(),.split())
print(a, b, c, d, e, f)
