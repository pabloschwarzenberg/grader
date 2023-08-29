#Aprobación de créditos
ingreso = int(input(" "))
fecha = int(input(" "))
hijos = int(input(" "))
membresia = int(input(" "))
estado_civil = input(" ")
vivienda = input(" ")
if ingreso > 10 and hijos >= 2:
  print("APROBADO")
elif estado_civil == "C" and hijos > 3 and fecha >= 1962 and fecha <= 1972:
  print("APROBADO")
elif ingreso > 2500000 and estado_civil == "S" and vivienda == "C":
  print("APROBADO")
elif ingreso > 3500000 and membresia > 5:
  print("APROBADO")
elif vivienda == "R" and estado_civil == "C" and hijos < 2:
  print("APROBADO")
else:
  print("RECHAZADO")