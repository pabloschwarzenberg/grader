#Sistema de Ecuaciones
print("En el uso de este programa, utilice la formula: (ax + by = c) y (dx + ey = f) ")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))
e = float(input("e: "))
f = float(input("f: "))
det = a*e - b*d
def solucion(a, b, c, d, e, f):
    if det != 0:
        x = (c * e - b * f) / det
        y = (a * f - c * d) / det
        return print("x ="+str(x)),print("y ="+str(y))
    else:
        return None, None
print(solucion(a, b, c, d, e, f))