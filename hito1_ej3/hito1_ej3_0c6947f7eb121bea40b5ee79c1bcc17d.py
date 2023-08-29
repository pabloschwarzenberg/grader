#Aprobación de crédito
plata = int(input("ingrese ingresos: "))
año = int(input("año de nacimiento: "))
hijos = int(input("cuantos hijos tiene: "))
abanco = int(input("cuantos años lleva con este banco: "))
ecivil = input("su estado civil C o S ")
sector = input("U o R ")

edad = 2022 -  año

if abanco > 10 and hijos >=2:
  print("APROBADO")
elif ecivil == "C" and hijos > 3 and edad >= 45 and edad <= 55:
  print("APROBADO")
elif plata > 2500000 and ecivil == "S" and sector == "U":
  print("APROBADO")
elif plata > 3500000 and abanco > 5:
  print("APROBADO")
elif sector == "R" and ecivil == "C" and hijos < 2:
  print("APROBADO")
else:
  print("RECHAZADO")