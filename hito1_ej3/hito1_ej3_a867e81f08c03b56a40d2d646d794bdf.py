#Aprobación de créditos
ingreso = int(input("Introduzca su ingreso: $"))

while ingreso < 0:


  print("Ingreso inválido.")
  ingreso = int(input("Introduzca su ingreso: $"))

aNacimiento = int(input("Introduzca su año de nacimiento: "))

while aNacimiento < 0:

  print("Ingreso inválido.")
  aNacimiento = int(input("Introduzca su año de nacimiento: "))

nHijos = int(input("Introduzca su cantidad de hijos: "))

while nHijos < 0:

  print("Ingreso inválido.")
  nHijos = int(input("Introduzca su cantidad de hijos: "))

aPertenencia = int(input("Introduzca sus año(s)de pertenencia: "))

while aPertenencia < 0:

  print("Ingreso inválido.")
  aPertenencia = int(input("Introduzca sus año(s) de pertenencia: "))

eCivil = str(input("Introduzca su estado civil, soltero(S) o casado(C): "))

while eCivil != "S" and eCivil != "C":

  print("Ingreso inválido.")
  eCivil = str(input("Introduzca su estado civil, soltero(S) o casado(C): "))

residencia = str(input("Introduzca si vive en rural(R) o urbano(U): "))

while residencia != "R" and residencia != "U": 

  print("ingreso inválido")
  residencia = str(input("Introduzca si vive en rural(R) o urbano(U): "))

edad = 2021 - aNacimiento

if aPertenencia > 10 and nHijos >= 2: 
  print("APROBADO")

elif eCivil == "C" and nHijos > 3 and edad >= 45 and edad <= 55:

  print("APROBADO")

elif ingreso > 2500000 and eCivil == "S" and residencia == "U": 

  print("APROBADO")

elif ingreso > 3500000 and aPertenencia > 5:
  print("APROBADO")

elif residencia == "R" and eCivil == "C" and nHijos < 2: 

  print("APROBADO")

else:

  print("RECHAZADO")