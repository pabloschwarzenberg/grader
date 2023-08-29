#Aprobación de créditos
ingreso=int(input("Ingreso: $"))
nacimiento=int(input("Anho de nacimiento: "))
hijos=int(input("Numero de Hijos: "))
pertenencia=int(input("Anhos de pertenencia al banco: "))
civil=input("Estado civil: ")
vive=input("Lugar en que vive: ")
anhos=2017-nacimiento

if(((pertenencia>10)and(hijos>=2))or((civil=="C")and(hijos>3)and(45<=anhos<=55))or((ingreso>2500000)and(civil=="S")and(vive=="U"))or((ingreso>3500000)and(pertenencia>5))or((vive=="R")and(civil=="C")and(hijos<2))):
    print("APROBADO")
else:
    print("RECHAZADO")