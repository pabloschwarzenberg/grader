#Sistema de Ecuaciones
def determinante(a,b,c,d,e,f):
    det=(a*e)-(b*d)
    if det != 0:
        x = (e*c-b*f)/det
        y = (a*f-d*c)/det
    return x,y

a = float(input("ingrece 1er numero: "))
b = float(input("ingrece 2do numero: "))
c = float(input("ingrece 3er numero: "))
d = float(input("ingrece 4to numero: "))
e = float(input("ingrece 5to numero: "))
f = float(input("ingrece 6to numero: "))

g=determinante(a,b,c,d,e,f)
h=g[0]
i=g[1]
print("x=",g[0])
print("y=",g[1])