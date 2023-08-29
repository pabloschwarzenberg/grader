def sistema_de_ecuaciones(a, b, c, d, e, f):
    determinante = (a * e) - (b * d)

    if determinante != 0:
        x = ((c * e) - (b * f)) / determinante
        y = ((a * f) - (c * d)) / determinante
        return print("x="+str(x)+", y="+str(y))
    else:
        return None, None

print("Ingresa los valores: ")
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

sistema_de_ecuaciones(a,b,c,d,e,f)