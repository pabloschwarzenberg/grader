#Aprobación de créditos
ingreso = eval(input("ingrese su ingreso: "))
anodenacimiento = int(input("ingrese su año de nacimiento: "))
ndh = int(input("ingrese la cantidad de hijos que tiene: "))
anoenbanco = int(input("ingrese los años que lleva en el banco: "))
estadocivil = input("(S) : soltero, (C), casado: ")
vivienda = input(" vives en ciudad: (U), vives en campo (R): ")

while True:
  if anoenbanco>10:
    if ndh>=2:
      print("APROBADO")
      break
  if estadocivil == "C":
    if ndh>3:
      if(anodenacimiento - 2020)>= 45 and (anodenacimiento - 2020)<= 55:
        print ("APROBADO")
        break
  if ingreso>2500000:
    if estadocivil == "S":
      if vivienda == "U":
        print("APROBADO")
        break
  if ingreso>3500000:
    if anoenbanco>5:
      print("APROBADO")
      break
  if vivienda == "R":
    if estadocivil == "C":
      if ndh<3:
        print("APROBADO")
        break
  else:
    print("RECHAZADO")
    break