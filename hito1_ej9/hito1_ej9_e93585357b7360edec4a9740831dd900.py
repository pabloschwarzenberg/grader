def resolver_sistema(a, b, c, d, e, f):
    determinante = a * e - b * d
    if determinante == 0:
        return None  # El sistema no tiene solución única
    
    x = (c * e - b * f) / determinante
    y = (a * f - c * d) / determinante
    return round(x, 1), round(y, 1)

# Ejemplo de uso
a = 2
b = 3
c = 6
d = 1
e = 2
f = 5

soluciones = resolver_sistema(a, b, c, d, e, f)

if soluciones is None:
    print("El sistema no tiene solución única.")
else:
    x_sol, y_sol = soluciones
    print("Solución:")
    print("x=",{x_sol})
    print("y=",{y_sol})
