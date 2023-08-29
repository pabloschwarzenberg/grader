#Sistema de ecuaciones 
def solucion_sistema_ecuaciones(a, b, c, d, e, f):
    determinante= a*e - b*d

    if determinante != 0:
        x = (c*e - b*f) / determinante
        y = (a*f - c*d) / determinante
        print("x= ", x)
        print("y= ", y)
    else:
        print("no")


a = eval(input("Ingrese el valor de a: "))
b = eval(input("Ingrese el valor de b: "))
c = eval(input("Ingrese el valor de c: "))
d = eval(input("Ingrese el valor de d: "))
e = eval(input("Ingrese el valor de e: "))
f = eval(input("Ingrese el valor de f: "))
print(solucion_sistema_ecuaciones(a, b, c, d, e, f))  