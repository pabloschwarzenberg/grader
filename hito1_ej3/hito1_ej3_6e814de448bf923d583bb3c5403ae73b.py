#Aprobación de créditos
ingresos = int(input())
nacimiento = int(input())
hijos = int(input())
tiempo = int(input())
civil = str(input())
vivienda = str(input())

if tiempo > 10 and hijos >= 2:
  print("APROBADO")
elif civil == "C" and hijos > 3 and 55 >= (2017-nacimiento) >= 45:
  print("APROBADO")
elif ingresos > 2500000 and civil == "S" and vivienda == "U":
  print("APROBADO")
elif ingresos > 3500000 and tiempo > 5:
  print("APROBADO")
elif vivienda == "R" and civil == "C" and 2 > hijos:
  print("APROBADO")
else:
  print("RECHAZADO")







