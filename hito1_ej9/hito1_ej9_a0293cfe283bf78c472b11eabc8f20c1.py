a = int(input("Ingresa: "))
b = int(input("Ingresa: "))
c = int(input("Ingresa: "))
d = int(input("Ingresa: "))
e = int(input("Ingresa: "))
f = int(input("Ingresa: "))
def sistema_de_ecuaciones (a, b, c, d, e, f):
    determinante = a*e - b*d

    if determinante !=0:
        x = (c*e - b*f) / determinante
        y = (a*f - c*d) / determinante

        return print("x=",x,"y=",y)
    else:
        print("")
print(sistema_de_ecuaciones(a,b,c,d,e,f))