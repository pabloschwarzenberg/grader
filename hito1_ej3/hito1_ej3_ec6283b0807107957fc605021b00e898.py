#Aprobación de créditos
i = int(input("Ingresos: "))
an = int(input("Año de Nacimiento: "))
ndh = int(input("Numero de hijos: "))
ap = int(input("Años de pertenencia al banco: "))
ec = input("Estado civil (S: soltero, C, casado): ")
coc = input("Si vive en campo o cuidad ("U": urbano, "R": rural): ")
edad = 2020 - an

if ap > 10 and ndh >=2:
  print("APROBADO")
if ec == "C" and ndh > 3 and edad >=45 and edad <=55:
  print("APROBADO")
if i > 2500000 and ec == "S" and coc == "U":
  print("APROBADO")
if i > 3500000 and ec == "C" and ap > 5:
  print("APROBADO")
if coc == "R" and ec == "C" and ndh <2:
  print("APROBADO")
else:
  print("RECHAZADO")