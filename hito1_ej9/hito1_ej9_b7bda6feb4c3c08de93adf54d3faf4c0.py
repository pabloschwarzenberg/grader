def resolver_sistema(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1
    
    if determinante == 0:
        return None  # El sistema no tiene solución única
    
    x = (b2 * c1 - b1 * c2) / determinante
    y = (a1 * c2 - a2 * c1) / determinante
    
    return x, y

# Ejemplo de uso
a1, b1, c1 = 2, 3, 6
a2, b2, c2 = 1, 2, 5

solucion = resolver_sistema(a1, b1, c1, a2, b2, c2)

if solucion is not None:
    x, y = solucion
    print(f"x = {x:.1f}")
    print(f"y = {y:.1f}")
else:
    print("El sistema no tiene solución única")