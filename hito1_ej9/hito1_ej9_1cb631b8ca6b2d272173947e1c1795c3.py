#Sistema de Ecuaciones
print("elige los valores de las variables")
m=float(input(""))
n=float(input(""))
o=float(input(""))
p=float(input(""))
q=float(input(""))
r=float(input(""))
detreminante=((m*q)-(n*p))
if detreminante==1:
    x=((o*q)-(n*r))/detreminante
    y=((m*r)-(o*p))/detreminante
    print("x="+str(x),"y="+str(y))
else:
    print("no hay solucion")     