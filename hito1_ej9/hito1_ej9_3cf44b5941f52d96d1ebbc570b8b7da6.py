from sympy import symbols, Eq, solve

def resolver_sistema(a1, b1, c1, a2, b2, c2):
    x, y = symbols('x y')
    ecuacion1 = Eq(a1*x + b1*y, c1)
    ecuacion2 = Eq(a2*x + b2*y, c2)
    solucion = solve((ecuacion1, ecuacion2), (x, y))
    return solucion

a1 = 2
b1 = 3
c1 = 6
a2 = 1
b2 = 2
c2 = 5

solucion = resolver_sistema(a1, b1, c1, a2, b2, c2)

x_solucion = round(solucion[x], 1)
y_solucion = round(solucion[y], 1)

print(f"x = {x_solucion}")
print(f"y = {y_solucion}")