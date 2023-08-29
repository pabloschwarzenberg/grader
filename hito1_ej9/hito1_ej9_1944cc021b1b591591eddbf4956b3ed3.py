def solucion_sistema_ecuacionesx(a,b,c,d,e,f):
    determinante = a*e - b*d

    if determinante != 0:
        x = (c*e - b*f) / determinante
        return x

def solucion_sistema_ecuacionesy(a,b,c,d,e,f):
    determinante = a*e - b*d

    if determinante != 0:
        y = (a*f - c*d) / determinante
        return y


a = int(input("ingresa el primer numero: "))
b = int(input("ingresa el segundo numero: "))
c = int(input("ingresa el tercero numero: "))
d = int(input("ingresa el cuarto numero: "))
e = int(input("ingresa el quinto numero: "))
f = int(input("ingresa el sexto numero: "))
print('x=',solucion_sistema_ecuacionesx(a,b,c,d,e,f))
print('y=',solucion_sistema_ecuacionesy(a,b,c,d,e,f))