# Sistema de Ecuaciones
def solucion(a, b, c, d, e, f):
    determinante = a * e - b * d
    if determinante != 0:
        x = (c * e - b * f) / determinante
        y = (a * f - c * d) / determinante
        return round(x,1), round(y,1)
    return 0, 0

print("Digite los valores para  a,b,c,d,e,f:")
a = float(input("A:"))
b = float(input("B:"))
c = float(input("C:"))
d = float(input("D:"))
e = float(input("E:"))
f = float(input("F:"))
x=str(solucion(a,b,c,d,e,f))
y=str(solucion(a,b,c,d,e,f))
print("x=",x[1:5],"Y=",y[5:16])
