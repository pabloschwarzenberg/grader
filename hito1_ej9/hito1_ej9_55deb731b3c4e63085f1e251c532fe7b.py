#Sistema de Ecuaciones
print('Digite los valores para a, b, c, d, e, f: ')
a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))
d = float(input("Ingrese d: "))
e = float(input("Ingrese e: "))
f = float(input("Ingrese f: "))
def solución_sistema_ecuaciones(a,b,c,d,e,f):
    determinante = a*e - b*d

    if determinante != 0:
        x = (c * e - b * f) / determinante
        y = (a * f - c * d) / determinante
        return ["x= {} y =  {}" .format(x,y)]
    else:
        return None,None



print(solución_sistema_ecuaciones(a,b,c,d,e,f))