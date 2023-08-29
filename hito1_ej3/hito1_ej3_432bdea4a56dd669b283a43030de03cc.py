#Aprobación de créditos
Ingreso=int(input("Ingrese sueldo en pesos: "))
Nacimiento=int(input("Ingrese año de nacimiento (AAAA): "))
Hijos=int(input("Ingrese cantidad de hijos: "))
Pertenencia=int(input("Ingrese años de pertenencia: "))
Estado_civil=input("Ingrese Estado Civil C=casad@/S=solter@: ")
Residencia=input("Ingrese lugar de residencia U=urbano/R=rural: ")

Edad=2016-Nacimiento
Estado_civil=Estado_civil.upper()
Residencia=Residencia.upper()

if Pertenencia>10 and Hijos>=2:
  print("APROBADO")
if Estado_civil=="C" and Hijos>3 and 45<Edad<55:
  print("APROBADO")
if Ingreso>2500000 and Estado_civil is "S" and Residenia is "C":
  print("APROBADO")
if Ingreso>3500000 and Pertenencia>5:
  print("APROBADO")
if Residencia=="R" and Estado_civil=="C" and Hijos < 2:
  print("APROBADO")
else: 
  print("RECHAZADO")