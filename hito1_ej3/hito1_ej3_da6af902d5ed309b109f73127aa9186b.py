ingreso=int(input("Ingrese su ingreso en pesos:"))
nacimiento=int(input("Ingrese su año de nacimiento:"))
hijos=int(input("Ingrese su número de hijos:"))
pertenencia=int(input("Ingrese los años de pertenencia al banco:"))
estadocivil=input("Ingrese su estado civil:")
vivienda=input("¿Ud vive en campo o ciudad?")

año=2022-nacimiento

if pertenencia>10 and hijos>=2:
  print("APROBADO")
elif estadocivil=="C" and hijos>3 and año>45 and año<55:
  print("APROBADO")
elif estadocivil=="S" and ingreso>2500000 and vivienda<"U":
  print("APROBADO")
elif ingreso>3500000 and pertenencia>5:
  print("APROBADO")
elif estadocivil=="C" and vivienda=="R" and hijos<2:
  print("APROBADO")
else:
  print("RECHAZADO")