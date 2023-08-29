#Informacion requerida para el credito
ingreso = int(input("Ingrese sus ingresos: "))
ano = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese la cantidad de hijos que tiene: "))
anos_banco = int(input("Ingrese la cantidad de años que lleva en el banco: "))
estado_civil = input("Ingrese su estado civil : ")
donde_vive = input("Ingrese si vive en una zona urbana o rural: ")

edad = 2022 - ano

# Condiciones para aprobar o rechazar
if anos_banco > 10 and 2 <= hijos:
  print("APROBADO")

elif estado_civil == "C" and 3 < hijos and 45 <= edad <= 55:
  print("APROBADO")

elif 2500000 < ingreso and estado_civil == "S" and donde_vive == "U":
  print("APROBADO")

elif 3500000 < ingreso and 5 < anos_banco:
  print("APROBADO")

elif donde_vive == "R" and estado_civil == "C" and hijos < 2:
  print("APROBADO")

else:
  print("RECHAZADO")
