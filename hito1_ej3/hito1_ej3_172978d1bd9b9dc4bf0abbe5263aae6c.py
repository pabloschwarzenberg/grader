#Aprobación de créditos

#Un Banco desea implementar una política de atención automatizada de créditos de consumo, y te contrata para programar su servicio. Los postulantes entregarán al banco la siguiente información:
# Ingreso (en pesos)
# Año de nacimiento
# Número de hijos
# Años de pertenencia al banco
# Estado civil ("S": soltero, "C", casado)
# Si vive en campo o cuidad ("U": urbano, "R": rural)

# El banco usará las siguientes reglas para decidir la aprobación del crédito, con una de ellas que se cumpla, se aprueba el crédito:

# Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
# Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
# Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
# Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
# Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
# Tu programa debe preguntar sus datos al cliente, procesarlos, e imprimir el mensaje APROBADO o RECHAZADO según corresponda.


Ingreso = int(input("Ingrese su monto en pesos:"))
AnoNacimiento = int(input("Ingrese su año de nacimiento:"))
NumeroHijos = int(input("Ingrese cantidad de hijos:"))
AnosEnBanco = int(input("Ingrese años de pertenencia al banco]:"))
Estado = str(input("Ingrese si es Soltero (S) o casado (C):"))
CampoOCiudad = str(input("Ingrese si vive en campo (R) o ciudad (U):"))

AnoActual = 2022
Edad = AnoActual - AnoNacimiento

if AnosEnBanco > 10 and NumeroHijos >= 2:
  print("APROBADO")

if str(Estado) == "C" and NumeroHijos > 3 and Edad > 45 and Edad < 55:
  print("APROBADO")

if Ingreso > 2500000 and str(Estado) == "S" and str(CampoOCiudad) == "U":
  print("APROBADO")

if Ingreso > 3500000 and AnosEnBanco > 5:
  print("APROBADO")

if str(CampoOCiudad) == "R" and str(Estado) == "C" and NumeroHijos < 2:
  print("APROBADO")

