#Aprobación de créditos
credito = False
estado_civil = ""
donde_vive = ""
C = ""
S = ""
U = ""
R = ""

ingreso = int(input("escriba su ingreso en pesos:"))
fecha_nacimiento = int(input("ingrese su año de nacimiento:"))
num_hijos = int(input("ingrese su numero de hijos:"))
tiempo_pertenencia = int(input("ingrese la cantidad de años que ha pertenecido al banco:"))
while estado_civil != "S" and estado_civil != "C":
  estado_civil = input("ingrese su estado civil, S=soltero, C=casado:")
while donde_vive != "U" and donde_vive != "R":
  donde_vive = input("vive en un lugar urbano o rural?\nU=urbano, R=rural:")
if tiempo_pertenencia > 10 and num_hijos >= 2:
  print("APROBADO")
elif estado_civil == C and num_hijos > 3 and fecha_nacimiento >= 1967 and fecha_nacimiento <= 1977:
  print("APROBADO")
elif ingreso > 2500000 and estado_civil == S and donde_vive == U:
  print("APROBADO")
elif ingreso > 3500000 and tiempo_pertenencia > 5:
  print("APROBADO")
elif donde_vive == R and estado_civil == C and 2>num_hijos:
  print("APROBADO")
else:
  print("RECHAZADO")