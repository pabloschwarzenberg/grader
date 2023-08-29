#Sistema de Ecuaciones

a = eval(input("Ingrese el valor de a: "))
b = eval(input("Ingrese el valor de b: "))
c = eval(input("Ingrese el valor de c: "))
d = eval(input("Ingrese el valor de d: "))
e = eval(input("Ingrese el valor de e: "))
f = eval(input("Ingrese el valor de f: "))
determinante = a*e - b*d

if determinante !=0:
    x = (c*e - b*f) / determinante
    y = (a*f - c*d) / determinante 
    x1=round(x, 1)
    y2=round(y, 1)
    print("x=", x1)
    print("y=", y2)
else:
    print("Valor no valido, determinante es 0")      