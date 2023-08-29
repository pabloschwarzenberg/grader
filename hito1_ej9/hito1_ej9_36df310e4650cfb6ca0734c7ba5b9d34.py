#Sistema de Ecuaciones
print("Elige los valores de las variables")
a = float(input(""))
b = float(input(""))
c = float(input(""))
d = float(input(""))
e = float(input(""))
f = float(input(""))
determinante = a*e - b*d
if determinante != 0:
        x = (c*e -b*f)/ determinante
        y =(a*f -c*d)/ determinante
        print("x="+str(x),"y="+str(y))
else:
    print("No hay solucion")

