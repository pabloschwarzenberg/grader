def solucion(a, b, c, d, e, f):
    determ = a*e -  b*d
    if determ != 0:
        x = (c*e - b*f) / determ
        y = (a*f - c*d) / determ
        return x, y
    else:
        return None, None

num = input("Ingrese los valores de las ecuaciones: ").split()
a, b, c, e, d, f = list(map(lambda z: int(z), num))

x, y = solucion(a, b, c, e, d, f)
print("x=",x)
print("y=",y)