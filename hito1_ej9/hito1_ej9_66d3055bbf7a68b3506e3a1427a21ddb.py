#Sistema de Ecuaciones
def solucion_sistema_ecuaciones(a,b,c,d,e,f):
    determinante = a*e - b*d

    if determinante != 0:
        x=(c*e - b*f) / determinante
        y=(a*f - c*d) / determinante
        print("x= " + str(x))
        print("y= " + str(y))
        return x, y
    else:
        return None, None

a=float(input("Digite el valor a: "))
b=float(input("Digite el valor b: "))
c=float(input("Digite el valor c: "))
d=float(input("Digite el valor d: "))
e=float(input("Digite el valor e: "))
f=float(input("Digite el valor f: "))

print(solucion_sistema_ecuaciones(a,b,c,d,e,f))   