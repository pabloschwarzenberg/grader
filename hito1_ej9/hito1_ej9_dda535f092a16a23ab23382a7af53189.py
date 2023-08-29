import np:
def resolver_sistema(a, b, c, d, e, f):
    coeficientes = np.array([[a, b], [c, d]])
    constantes = np.array([e, f])
    soluciones = np.linalg.solve(coeficientes, constantes)
    return soluciones
a = 2
b = 3
c = 1
d = 2
e = 6
f = 5

soluciones = resolver_sistema(a, b, c, d, e, f)

x = round(soluciones[0], 1)
y = round(soluciones[1], 1)

print("x =", x)
print("y =", y)