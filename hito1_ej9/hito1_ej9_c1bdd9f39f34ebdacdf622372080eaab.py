#Sistema de Ecuaciones
print("Determina las variables")
m=float(input(""))
n=float(input(""))
o=float(input(""))
p=float(input(""))
q=float(input(""))
r=float(input(""))
deter=((m*q)-(n*p))
if deter==1:
    x=((o*q)-(n*r))/deter
    y=((m*r)-(o*p))/deter
    print("x="+str(x),"y="+str(y))
else:
    print("no hay solucion")

