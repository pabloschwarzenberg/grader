#Aprobación de créditos

ingresos = int(input("Ingrese los ingresos que tiene: "))
nacimiento = int(input("Ingrese el año en que nació: "))
numeroHijos = int(input("Ingrese el número de hijos: "))
pertenencia = int(input("Ingrese la cantidad de años que lleva en el banco: "))
estadoCivil = str(input("Ingrese su estado civil, S si es solter@ o C si es casad@"))
vive = str(input("Ingrese si viva en campo o ciudad, U si vive en ciudad o R en un lugar rural: "))
i = False
edad = 2022 - nacimiento

while i == False:
  if pertenencia > 10 and numeroHijos >= 2:
    print("APROBADO")
    i = True
  elif estadoCivil == "C" and numeroHijos > 3 and edad >= 45 and edad <= 55:
    print("APROBADO")
    i = True
  elif ingresos > 2500000 and estadoCivil == "S" and vive == "U":
    print("APROBADO")
    i = True
  elif ingresos > 3500000 and pertenencia > 5:
    print("APROBADO")
    i = True
  elif vive == "R" and estadoCivil == "C" and numeroHijos < 2:
    print("APROBADO")
    i = True
  else:
    print("RECHAZADO")
    i = True