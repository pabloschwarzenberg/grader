#Aprobación de créditos
#Ingreso (en pesos)
#Año de nacimiento
#Número de hijos
#Años de pertenencia al banco
#Estado civil ("S": soltero, "C", casado)
#Si vive en campo o cuidad ("U": urbano, "R": rural)
#U = ciudad
#R = campo

#Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
#Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
#Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
#Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
#Si el cliente vive en el campo, es casado y tiene menos de dos hijos.

print("SISTEMA APROBACION DE CREDITOS")
nombre = ("Ingrese su nombre: ")
año_nacimiento = int(input("Ingrese su año de nacimiento: "))
edad = 2022 - año_nacimiento
estado_civil = input("Ingrese su estado civil, S o C: ")
numero_hijos = int(input("Ingrese la cantidad de hijos: "))
vivienda = input("Ingrese si vive en campo o ciudad, U o R: ")
ingreso = int(input("Ingrese sus ingresos en pesos: $"))
años_banco = int(input("Ingrese sus años en el banco: "))
if años_banco > 10:
  if numero_hijos >=2:
    print("APROBADO")
elif estado_civil == "C":
  if numero_hijos > 3:
    if edad >= 45 and edad <= 55:
      print("APROBADO")
elif ingreso > 2500000:
  if estado_civil == "S":
    if vivienda == "U":
      print("APROBADO")
elif ingreso > 3500000:
  if años_banco > 5:
    print("APROBADO")
elif vivienda == "R":
  if estado_civil == "c":
    if numero_hijos < 2:
      print("APROBADO")
else:
  print("RECHAZADO")      