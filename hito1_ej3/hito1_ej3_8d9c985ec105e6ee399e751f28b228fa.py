#Aprobación de créditos
ingreso=int(input("ingreso (en pesos): "))
ano_nacimiento=int(input("año de nacimiento: "))
hijos=int(input("numero de hijos: "))
anos_pertenencia=int(input("años de pertenencia al banco: "))
estado_civil=input("estado civil (S:soltero, C:casado): ")
vive=input("si vive en campo o ciudad (U:urbano, R:rural): ")
anos=2021-ano_nacimiento

if anos_pertenencia>10 and hijos>=2:
    credito="APROBADO"

elif estado_civil.upper()=="C" and hijos>3 and anos>=45 and anos<=55:
    credito="APROBADO"

elif ingreso>2500000 and estado_civil.upper()=="S" and vive.upper()=="U":
    credito="APROBADO"

elif ingreso>3500000 and anos_pertenencia>5:
    credito="APROBADO"

elif vive.upper()=="R" and estado_civil.upper()=="C" and hijos<2:
    credito="APROBADO"

else:
    credito="RECHAZADO"

print(credito)
