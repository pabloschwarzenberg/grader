#Sistema de Ecuaciones
from sympy import symbols, Eq, solve

def resolver_sistema(a, b, c, d, e, f):
    x, y = symbols('x y')
    ecuacion1 = Eq(a*x + b*y, c)
    ecuacion2 = Eq(d*x + e*y, f)
    solucion = solve((ecuacion1, ecuacion2), (x, y))
    x_sol = round(solucion[x], 1)
    y_sol = round(solucion[y], 1)
    return x_sol, y_sol

# Ejemplo de uso
a = 2
b = 3
c = 6
d = 1
e = 2
f = 5

x_solucion, y_solucion = resolver_sistema(a, b, c, d, e, f)
print(f'x = {x_sol}')
print(f'y = {y_sol}')
      