#Aprobación de créditos
ingreso=int(input("Coloque el total de ingresos: "))
ano_nac=int(input("Coloque el Año de nacimiento: "))
num_hijos=int(input("Coloque su Número de hijos: "))
anos_banco=int(input("Coloque el total de Años de pertenencia al banco: "))
est_civil=input("Coloque su Estado civil : (S)soltero, , (C)casado: ")
vivienda=input("Coloque si vive en campo o cuidad (U): urbano, (R): rural): ")
edad=2022- ano_nac
#Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos
if anos_banco>10 and num_hijos>=2: 
  print("APROBADO")
#Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
if est_civil=="C" and num_hijos==3 and 45<edad<55:
  print("APROBADO")
#Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
if ingreso > 2500000 and est_civil=="S" and vivienda=="U":
  print("APROBADO")
#Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
if ingreso > 3500000 and anos_banco>5: 
  print("APROBADO")
#Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
if vivienda=="R" and est_civil=="C" and num_hijos<2:
  print("APROBADO")
else: 
  print("REPROBADO")      