#Sistema de Ecuaciones
def solucion(a,b,c,d,e,f):
    determinante = a*e - b*d
    if determinante != 0:
        x = (c * e - b * f) / determinante
        y = (a * f - c * d) / determinante

        print("x=",x,"y=",y)
    else:
        return None, None
print("Ingrese los términos a ,b ,c ,d ,e ,f del sistema de ecuaciones :")
a = int(input("Ingrese el término a: "))
b = int(input("Ingrese el término b: "))
c = int(input("Ingrese el término c: "))
d = int(input("Ingrese el término d: "))
e = int(input("Ingrese el término e: "))
f = int(input("Ingrese el término f: "))

print(solucion(a,b,c,d,e,f))

      