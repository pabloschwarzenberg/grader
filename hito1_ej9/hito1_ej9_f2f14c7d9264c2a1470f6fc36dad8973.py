def resolver_sistema(a, b, c, d, e, f):
    determinante = a * d - b * c
    if determinante == 0:
        return None  # El sistema no tiene solución única
    else:
        x = (e * d - b * f) / determinante
        y = (a * f - c * e) / determinante
        return x, y


# Pedir al usuario los coeficientes del sistema
a, b, c, d, e, f = map(float, input("Ingrese los coeficientes del sistema separados por espacios: ").split())

# Resolver el sistema
solucion = resolver_sistema(a, b, c, d, e, f)

# Imprimir la solución redondeada a un decimal, si existe
if solucion is None:
    print("El sistema no tiene solución única.")
else:
    x, y = solucion
    print(f"x={round(x, 1)}")
    print(f"y={round(y, 1)}")

