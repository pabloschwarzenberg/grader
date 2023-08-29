#Aprobación de créditos
ingreso = int(input())
Nacimiento = int(input())
NHijos = int(input())
APB = int(input())
Estadocivil = input()
CampooCiudad = input()

if APB > 10 and NHijos >=2:
  print("APROBADO")
elif Estadocivil == "C" and NHijos >3 and Nacimiento >=45 and Nacimiento <=55:
  print("APROBADO")
elif ingreso >2500000 and Estadocivil == "S" and CampooCiudad == "U":
  print("APROBADO")
elif ingreso >3500000 and APB >5:
  print("APROBADO")
elif CampooCiudad == "R" and Estadocivil == "C" and NHijos < 2:
  print("APROBADO")
else:
  print("APROBADO")