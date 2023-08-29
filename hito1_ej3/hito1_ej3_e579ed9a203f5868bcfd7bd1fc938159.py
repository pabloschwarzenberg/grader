#Aprobación de créditos
i= int(input("ingresos:"))
an=int(input("año de nacimiento:"))
nh=int(input("numero de hijos:"))
ap=int(input("años de pertenencia al banco:"))
ec=input("(S:soltero,C:casado):")
v=input("(U:urbano,R:rural)")


if (ap>10) and (nh>=2):
    print("APROBADO")
elif (ec=='C') and (nh>3) and (an>=1965 and an<=1975):
    print("APROBADO")
elif (i>2500000) and (ec=='S') and (v=='U'):
    print("aprobado")
elif (i>3500000)and(ap>5):
    print("aprobado")
elif (v=='R')and (ec=='C') and (nh<2):
    print("APROBADO")
else:
    print("RECHAZADO")