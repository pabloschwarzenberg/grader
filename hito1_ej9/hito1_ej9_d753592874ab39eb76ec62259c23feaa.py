#Sistema de Ecuaciones
a=float(input("Ingrese el número: "))
b=float(input("Ingrese el número: "))
c=float(input("Ingrese el número: "))
D=float(input("Ingrese el número: "))
E=float(input("Ingrese el número: "))
F=float(input("Ingrese el número: "))

#DESARROLLO DEL SISTEMA DE ECUACIONES#

b2=b*D
c2=c*D
E2=E*a
F2=F*a

y=(c2-F2)/(b2-E2)
x=(c-(b*y))/a

#print("x=",x)
#print("y=",y)

print("x=",x,"y=",y)
