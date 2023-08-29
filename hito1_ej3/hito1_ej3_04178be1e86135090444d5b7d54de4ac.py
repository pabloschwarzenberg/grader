#Aprobación de créditos
pesos = int(input())
anacimiento = int(input())
nhijos = int(input())
abanco = int(input())
estado_civil = input().capitalize()
vive = input().capitalize()
edad = 2022 - anacimiento

if abanco > 10 and nhijos >= 2:
  print("APROBADO")
elif estado_civil == "C" and nhijos > 3 and edad >= 45 and edad <= 55:
  print("APROBADO")
elif pesos > 2500000 and estado_civil == "S" and vive == "U":
  print("APROBADO")
elif pesos > 3500000 and abanco > 5:
  print("APROBADO")
elif vive == "R" and estado_civil == "C" and nhijos < 2:
  print("APROBADO")
else:
  print("RECHAZADO")