#Aprobación de créditos
ingresos = int(input())
nacimiento = int(input())
hijos = int(input())
anos = int(input())
civil = input()
vivienda = input()

if civil == "S":
  casado = False
else:
  casado = True 
  
if anos > 10 and hijos >= 2:
  credito = True
elif casado and hijos > 3 and edad >= 45 and edad <= 55:
  credito = True
elif ingresos > 2500000 and civil == "S" and vivienda == "U":
  credito = True 
elif ingresos > 3500000 and anos > 5:
  credito = True 
elif vivienda == "R" and casado and hijos < 2:
  credito = True
else:
  credito = False 

if credito:
  print("APROBADO")
else:
  print("RECHAZADO")