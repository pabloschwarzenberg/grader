#Aprobación de créditos
ing = int(input("Ingreso (en pesos): "))
año = int(input("Año de nacimiento: "))
hijos = int(input("Número de hijos: "))
años_banco = int(input("Años de pertenencia al banco"))
estado_civil = str(input("Estado civil ('S': soltero, 'C', casado) :"))
vivienda = str(input("Si vive en campo o cuidad ('U': urbano, 'R': rural): "))
edad = 2022-año

if años_banco > 10 and hijos >= 2:
  print("APROBADO")
if estado_civil == "C" and hijos >= 3 and 45 < edad < 55:
  print("APROBADO")
elif ing > 2500000 and estado_civil == "S" and vivienda == "U":
  print("APROBADO")
elif ing > 3500000 and años_banco > 5:
  print("APROBADO")
elif vivienda == "R" and estado_civil == "C" and hijos < 2:
  print("APROBADO")
else:
  print("RECHAZADO")      