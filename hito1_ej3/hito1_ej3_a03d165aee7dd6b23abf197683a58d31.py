ingreso=int(input("Ingreso (en pesos): "))
ano=int(input("Año de nacimiento: "))
hijos=int(input("Número de hijos: "))
pertenencia=int(input("Años de pertenencia al banco: "))
e_civil=str(input("Estado civil (S: Soltero, C: Casado: "))
vivienda=str(input("Vive en el campo o la ciudad (U: urbano, R: rural: "))

if pertenencia>10 and hijos>=2:
    credito="APROBADO"
elif e_civil =="C" and hijos>3 and ano>1976 and ano<1966:
    credito="APROBADO"
elif ingreso > 2500000 and e_civil=="S" and vivienda=="U":
    credito="APROBADO"
elif ingreso > 3500000 and pertenencia>5:
    credito="APROBADO"
elif vivienda=="R" and e_civil=="C" and hijos<2:
    credito="APROBADO"
else:
    credito="RECHAZADO"
print(credito)

