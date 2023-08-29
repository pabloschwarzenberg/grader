#Sistema de Ecuaciones
print("elige los valores de las variables")
m=float(input(""))
n=float(input(""))
o=float(input(""))
p=float(input(""))
q=float(input(""))
r=float(input(""))

determinante=((m*q)-(n*p))

if determinante==1:
    x=((o*q)-(n*r))/determinante
    y=((m*r)-(o*p))/determinante
    print("x="+str(x),"y="+str(y))
else:
    print("No Hay solucion")