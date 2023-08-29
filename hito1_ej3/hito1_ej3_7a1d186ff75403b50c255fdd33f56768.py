#Aprobación de créditos
ingreso = int(input("ingresos"))
nacimiento = int(input("año de nacimiento"))
hijos = int(input("cantidad de hijos"))
pertenencia = int(input("cuanto tiempo ha pertenecido al banco"))
estado_civil = input("soltero o casado")
vivienda = input("urbano o rural")
edad = 2022-nacimiento

if pertenencia > 10 and hijos>=2:
  print("APROBADO")
elif estado_civil =="C" and hijos>3 and edad>=45 and edad <=55:
  print("APROBADO")
elif ingreso >2500000 and estado_civil == "S" and vivienda == "U":
  print("APROBADO")
elif ingreso >3500000 and pertencia > 5:
  print("APROBADO")
elif vivienda =="R" and estado_civil=="C" and hijos <2:
  print("APROBADO")
else:
  print("RECHAZADO")