#Aprobación de créditos
ingreso = int(input("ingreso: "))
nacimiento = int(input("ingresa tu año de nacimiento: "))
numhijos = int(input("ingresa numeros de hijos: "))
pertenciaBanco = int(input("ingresa años de pertenencia al banco: "))
estadoCivil = input("ingrese estado civil S:soltero o C:casado: ")
dondeVive = input("ingrese si vive en U:Urbano o R:Rural : ")

if(pertenciaBanco > 10 and numhijos>= 2):
   print("APROBADO")
else:
  print("RECHAZADO")
if(estadoCivil == "C" and numhijos > 3 and nacimiento < 1967 and nacimiento > 1977):
  print("APROBADO")
else:
  print("RECHAZADO")
if(estadoCivil == "S" and ingreso >2500000 and dondeVive == "U"):
  print("APROBADO")
else:
  print("RECHAZADO")
if(ingreso > 3500000 and perteneciaBanco > 5):
  print("APROBADO")
else:
  print("RECHAZADO")
if(dondeVive == "R" and estadoCivil == "C" and numhijos < 2):
  print("APROBADO")
else:
  print("RECHAZADO")
  