ingresos = int(input("Ingresos"))
nacimiento = int(input("nacimiento"))
hijos = int(input("hijos"))
pertenencia = int(input("Pertenencia"))
estadocivil = input("estado civil S o C ")
vive = input("urbano o rural U o R")

edad = 2022-nacimiento

if pertenencia>10 and hijos>=2:
  print("APROBADO")
elif estadocivil == "C" and hijos>3 and edad>=45 and edad<=55:
  print("APROBADO")
elif ingresos>2500000 and estadocivil=="S" and vive=="U":
  print("APROBADO")
elif ingresos>3500000 and pertenencia>5:
  print("APROBADO")
elif vive=="R" and estadocivil=="C" and hijos<2:
  print("APROBADO")
else:
  print("RECHAZADO")