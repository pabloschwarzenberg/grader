#Sistema de Ecuaciones
def solucion_sistema_ecuaciones(a,b,c,d,e,f):
    determinante = (a*e) - (b*d)
    if determinante != 0 :
        x = (c*e - b*f)/determinante
        y = (a*f - c*d)/determinante
        print("x=" + str(x))
        print("y=" + str(y))
    else:
        return None ,None

print("digite los valores para a,b,c,d,e,f:  ")
a = int(input("ingrese el valor de a: "))
b = int(input("ingrese el valor de b: "))
c = int(input("ingrese el valor de c: "))
d = int(input("ingrese el valor de d: "))
e = int(input("ingrese el valor de e: "))
f = int(input("ingrese el valor de f: "))

print(solucion_sistema_ecuaciones(a,b,c,d,e,f))
