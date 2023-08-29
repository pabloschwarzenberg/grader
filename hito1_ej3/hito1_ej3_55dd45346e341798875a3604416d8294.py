#Aprobación de créditos
ingreso = int(input("Indique su ingreso (en pesos)."))
nacimiento =  int(input("Indique su año de nacimiento:"))
hijos = int (input("Indique su número de hijos:"))
pertenencia = int(input("Indique sus años de pertenecia en el banco:"))
e_civil = input("Indique su estado civil:")
vivienda = input("Indique si vive en el campo o la ciudad:")
edad = 2022 - nacimiento
if pertenencia > 10 and hijos >= 2:
  print("APROBADO")
elif e_civil == "C" and hijos > 3 and  edad >= 45 and edad <= 55:
  print("APROBADO")
elif ingreso > 2500000 and e_civil == "S" and vivienda == "U":
  print("APROBADO")
elif ingreso > 3500000 and pertenencia > 5:
  print("APROBADO")
elif vivienda == "R" and e_civil == "C" and hijos < 2:
  print("APROBADO")
else:
  print("RECHAZADO")