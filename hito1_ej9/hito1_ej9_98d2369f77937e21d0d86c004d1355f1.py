#Sistema de Ecuaciones
s=int(input("Ingrese Valor:"))
k=int(input("Ingrese Valor:"))
l=int(input("Ingrese Valor:"))
s1=int(input("Ingrese Valor:"))
k1=int(input("Ingrese Valor:"))
l1=int(input("Ingrese Valor:"))
vlr=(s*k1 - k*s1)
if(vlr!=0):
    x=(l*k1-k*l1)/vlr
    y=(s*l1-l*s1)/vlr
    print("x=",x,"y=",y)