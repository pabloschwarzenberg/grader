from sympy import symbols, Eq, solve

def resolver_sistema(a, b, c, d, e, f):
    x, y = symbols('x y')
    
    ecuacion1 = Eq(a*x + b*y, c)
    ecuacion2 = Eq(d*x + e*y, f)
    
    solucion = solve((ecuacion1, ecuacion2), (x, y))
    
    return solucion[x].evalf(), solucion[y].evalf()


a = []
b = []
c = []
d = []
e = []
f = []

solucion_x, solucion_y = resolver_sistema(a, b, c, d, e, f)

print(f'x = {solucion_x:.1f}, y = {solucion_y:.1f}')
