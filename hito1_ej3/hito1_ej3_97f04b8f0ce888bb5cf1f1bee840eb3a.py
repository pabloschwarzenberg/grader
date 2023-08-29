#Aprobación de créditos
Ingreso = int(input())
Nacimiento = int(input())
Edad = 2022 - Nacimiento
Hijos = int(input())
Pertenencia = int(input())
Civil = input()
Vive = input()
if Pertenencia > 10 and Hijos >= 2:
  print("APROBADO")
elif Civil == "C" and Hijos > 3 and Edad >= 45 and Edad <= 55:
  print("APROBADO")
elif Ingreso > 2500000 and Civil == "S" and Vive == "U":
  print("APROBADO")
elif Ingreso > 3500000 and Pertenencia > 5:
  print("APROBADO")
elif Vive == "R" and Civil == "C" and Hijos < 2:
  print("APROBADO")
else:
  print("RECHAZADO")