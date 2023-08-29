
def resolver_sistema(a, b, c, d, e, f):
    x, y = symbols('x y')

    ecuacion2 = Eq(d*x + e*y, f)
    solucion = solve((ecuacion1, ecuacion2), (x, y))
    return solucion[x], solucion[y]

# Ejemplo de uso
solucion_x, solucion_y = resolver_sistema(2, 3, 6, 1, 2, 5)
print("x =", round(solucion_x, 1))
print("y =", round(solucion_y, 1))


      