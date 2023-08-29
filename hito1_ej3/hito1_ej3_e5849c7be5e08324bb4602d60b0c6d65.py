#Aprobación de créditos
ingreso = int(input("ingresos: "))
ano_n = int(input("año de nacimiento: "))
anos_tiene = ano_n - 2020
n_hijos = int(input("numero de hijos: "))
anospe = int(input("años de pertenencia al banco: "))
ecivil = input("[S] soltero, [C] casado")
casa = input("lugar de su hogar,[U] urbano, [R] rural: ")
if anospe >= 10 and n_hijos >= 2:
  print("APROBADO")
if ingreso >= 2500000 and ecivil == "S" and casa == "U":
  print("APROBADO")
#Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
if ecivil == "C" and n_hijos > 3 and anos_tiene < 55 > 44:
  print("APROBADO")
#Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
if ingreso >= 3500000 and anospe >= 5:
  print("APROBADO")
#Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
if casa == "R" and ecivil == "C" and n_hijos < 2:
  print("APROBADO")
else:
  print("RECHAZADO")