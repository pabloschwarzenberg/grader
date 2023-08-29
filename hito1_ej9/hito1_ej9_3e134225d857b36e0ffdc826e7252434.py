#Sistema de Ecuaciones
def sistema_de_ecuaciones(a,b,c,d,e,f):
    determinante = a*e - b*d

    if determinante !=0:
        x = (c*e - b*f)/determinante
        y = (a*f - c*d)/determinante
    print("x=" + str(x))
    print("y=" + str(y))
    return x, y

#a,b,c,d,e,f = map(float,input().split())
a=int(input("Ingrese el valor de a: "))
b=int(input("Ingrese el valor de b: "))
c=int(input("Ingrese el valor de c: "))
d=int(input("Ingrese el valor de d: "))
e=int(input("Ingrese el valor de e: "))
f=int(input("Ingrese el valor de f: "))
print(sistema_de_ecuaciones(a,b,c,d,e,f))