#Aprobación de créditos
## malditas variables
ingresos=int(input("favor ingrese sus ingresos:"))
nacimiento=int(input("favor ingrese su año de nacimiento:"))
hijos=int(input("favor ingrese numeros de hijos que tenga:"))
pertenece=int(input("favor ingrese cuantos años a permanecido al banco:"))
civil=input("favor ingrese su estado civil(la letra (S):soltero, letra (C):casado:").capitalize()
vive=input("favor ingrese donde vive con la letra (U):Urbano, letra (R): Rural:)").capitalize()
nuestro_ano=2022
ano_real=(nuestro_ano-nacimiento)
##ifeeesss

if pertenece>10 and hijos>=2 :
    print("APROBADO")
elif civil=="C" and hijos>3 and ano_real>=45 or ano_real<=55:
    print("APROBADO")
elif ingresos>2500000 and civil=="S" and vive=="U":
    print("APROBADO")
elif ingresos>3500000 and pertenece>5:
    print("APROBADO")
elif vive=="U" and civil=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")