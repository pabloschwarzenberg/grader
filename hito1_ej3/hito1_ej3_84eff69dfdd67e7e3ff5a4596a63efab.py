#Aprobación de créditos
Ingreso=int(input())
nacimiento=int(input())
hijos=int(input())
pertenencia=int(input())
Estado=str(input())
vive=str(input())

if  pertenencia>10 and hijos>=2:
    print("APROBADO")
elif Estado=="C" and hijos>3 and (2020-nacimiento)>45 and (2020-nacimiento)<55:
    print("APROBADO")
elif Ingreso>2500000 and Estado=="S" and vive=="U":
    print("APROBADO")
elif Ingreso>3500000 and pertenencia>5:
    print("APROBADO")
elif vive=="R" and Estado=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")