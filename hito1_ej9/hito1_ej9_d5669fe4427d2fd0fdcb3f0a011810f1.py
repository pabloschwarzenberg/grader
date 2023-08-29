#Sistema de Ecuaciones
def resolver_sistema(a, b, c, d, e, f):
    x = (c * e - b * f) / (a * e - b * d)
    y = (a * f - c * d) / (a * e - b * d)
    return x, y

# Ejemplo: 2x + 3y = -6 y x + 2y = -4
a = 2
b = 3
c = -6
d = 1
e = 2
f = -4

x, y = resolver_sistema(a, b, c, d, e, f)

# Imprimir las soluciones redondeadas a un decimal
x = round(x, 1)
y = round(y, 1)

print('x =', x)
print('y =', y)




      