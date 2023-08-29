#Aprobación de créditos
ingreso = int(input("ingrese sus ingresos: "))
nacimiento = int(input("su año de nacimiento: "))
hijos = int(input("ingrese la cantidad  de hijos que tiene: "))
pertenencia = int(input("años que lleva en el banco: "))
civil = input("estado civil (soltero = S / C = casado): ")
residencia = input("donde vive U = URBANO R = RURAL: ")
edad = 2022 - nacimiento 

if pertenencia > 10 and hijos >= 2:
  print("APROBADO")
elif civil == "C" and hijos > 3 and edad >= 45 and edad <= 55:
  print("APROBADO")
elif ingreso > 2500000 and civil == "C" and residencia == "U":
  print("APROBADO")
elif ingreso > 3500000 and pertenencia > 5:
  print("APROBADO")
elif residencia == "R" and civil == "C" and hijos < 2:
  print("APROBADO")
else:
  print("RECHAZADO")     