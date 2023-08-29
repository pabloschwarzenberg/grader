from sympy import symbols, Eq, solve

def resolver_sistema(a1, b1, c1, a2, b2, c2):
    x, y = symbols('x y')
    
    ecuacion1 = Eq(a1*x + b1*y, c1)
    ecuacion2 = Eq(a2*x + b2*y, c2)
    
    soluciones = solve((ecuacion1, ecuacion2), (x, y))
    
    solucion_x = round(soluciones[x], 1)
    solucion_y = round(soluciones[y], 1)
    
    return solucion_x, solucion_y

# Ejemplo de uso
coeficientes = [float(input("Ingrese el coeficiente a1: ")),
                float(input("Ingrese el coeficiente b1: ")),
                float(input("Ingrese el término c1: ")),
                float(input("Ingrese el coeficiente a2: ")),
                float(input("Ingrese el coeficiente b2: ")),
                float(input("Ingrese el término c2: "))]

solucion_x, solucion_y = resolver_sistema(*coeficientes)
print("Solución x:", solucion_x)
print("Solución y:", solucion_y)
