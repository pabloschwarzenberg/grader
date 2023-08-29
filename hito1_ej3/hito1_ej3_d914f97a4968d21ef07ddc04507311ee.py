Ingreso = int(input("ingrese su ingreso en pesos: ")) 
Nacimiento = int(input("ingrese su año de naciomiento: "))
Hijos = int(input("Cuantos hijos tiene: "))
AINB = int(input("Cuantos años lleva en el banco: "))
EC = input("Estado civil S (soltero), C(casado): ")
live = input("Si vive en campo o cuidad ("U": urbano, "R": rural)")

edad = Nacimiento - 2023

if AINB >= 10 and Hijos >= 2:
  print("APROBADO")
elif EC == "C" and Hijos >= 3 and edad >= 45 and edad <= 55:
  print("APROBADO")
elif Ingreso > 2500000 and EC == "S" and live == "U":
  print("APROBADO")
elif Ingreso > 3500000 and AINB > 5:
  print("APROBADO")
elif live == "R" and EC == "C" and Hijos < 2: 
  print("APROBADO")
else:
  print("RECHAZADO")