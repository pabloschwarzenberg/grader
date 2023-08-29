#Aprobación de crédito
ingreso = int(input())
nacimiento = int(input())
hijos = int(input())
pertenencia = int(input())
estado = input()
vivienda = input()
edad = 2018-nacimiento
if pertenencia>10 and hijos>= 2:
  print("APROBADO")
if estado=="C" and hijos>3 and (edad>45 and edad<55):
  print("APROBADO")
if ingreso>2500000 and estado=="S" and vivienda =="R":
  print("APROBADO")
if ingreso>3500000 and pertenencia>5:
  print("APROBADO")
if vivienda=="R" and estado=="C" and hijos<2:
  print("APROBADO")
else:
  print("RECHAZADO")
