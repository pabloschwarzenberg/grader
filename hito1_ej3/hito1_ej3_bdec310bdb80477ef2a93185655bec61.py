#Aprobación de créditos
ingreso = int(input("Ingrese los ingresos en pesos: "))
A_nacimiento = int(input("Ingrese el año de nacimiento: "))
hijos = int(input("Ingrese el número de hijos: "))
A_bancos = int(input("Ingrese los años de pertenencia al banco: "))
estadoCivil = input("Inrese el estado civil (S:soltero, C:casado): ")
vive = input("Vive en (U:urbano, R:rural): ")
edad = 2020 - A_nacimiento
if A_bancos >10 and 2 <= hijos:
 print("APROBADO")
else:
 if estadoCivil == "C" and 3 < hijos and 45 <= edad <= 55:
  print("APROBADO")
 else:
  if ingreso> 3500000 and A_bancos > 5:
   print("APROBADO")
  else:
   if vive == "R" and estadoCivil == "C" and hijos < 2:
    print("APROBADO")
   else:
       print("RECHAZADO")      