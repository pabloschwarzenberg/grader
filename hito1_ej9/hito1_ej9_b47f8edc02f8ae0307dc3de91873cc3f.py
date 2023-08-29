def sistema_ecuaciones(a, b, c, d, e, f):
    x = (c * e - b * f) / (a * e - b * d)
    y = (a * f - c * d) / (a * e - b * d)
    result = ['x={}'.format(round(x, 1)), 'y={}'.format(round(y, 1))]
    return result
a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))
d = float(input("Ingrese d: "))
e = float(input("Ingrese e: "))
f = float(input("Ingrese f: "))

resultados = sistema_ecuaciones(a, b, c, d, e, f)

for resultado in resultados:
    print(resultado)