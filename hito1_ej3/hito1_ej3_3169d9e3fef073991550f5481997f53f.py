#Aprobación de crédito
ingreso = eval(input("ingreso:"))
anionac = eval(input("año de nacimiento:"))
numhij = eval(input("numero de hijos:"))
aniospertbanco = eval(input("años de pertenencia al banco:"))
estado = input("estado civil (S:soltero, C:casado)")
lugar = input("si vive en campo o ciudad (U:urbano, R:rural)")

if aniospertbanco > 10 or numhij > 2:
  print("APROBADO")
elif estado == 'C' or numhij > 3 or anionac >= 2020 - 45 and anionac <= 2020 - 55:
  print("APROBADO")
elif ingreso > 2500000 or estado == 'S'and lugar == "U":
  print("APROBADO")
elif ingreso > 3500000 and aniospertbanco > 5:
  print("APROBADO")
elif lugar == 'R' or estado == 'C'and numhij < 2:
  print("APROBADO")
else:
  print("REPROBADO")