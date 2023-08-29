#Aprobación de créditos
ingreso = int(input())
a_nacimiento = int(input())
n_hijos = int(input())
a_prestancia = int(input())
e_civil = input()
vivienda = input()  

if a_prestancia > 10 and n_hijos >= 2:
  print("APROBADO")
elif e_civil == "C" and n_hijos > 3 and 45 <= (2016 - a_nacimiento) <= 55:
  print("APROBADO")
elif ingreso > 2500000 and e_civil == "S" and vivienda == "U":
  print("APROBADO")
elif ingreso > 3500000 and a_pertenencia > 5:
  print("APROBADO")
elif vivienda == "R" and e_civil == "C" and n_hijos < 2:
  print("APROBADO")
else:
  print("RECHAZADO")