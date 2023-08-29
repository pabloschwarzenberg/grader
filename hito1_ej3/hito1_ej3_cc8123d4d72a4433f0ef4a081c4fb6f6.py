#Aprobación de créditos
ingresos = int(input("escriba su ingreso(en pesos):"))
nacimiento = int(input("ingrese su año de nacimiento:"))
hijos = int(input("ingrese el numero de hijos:"))
anos = int(input("ingrese el nro de años de pertenencia al banco:"))
estado_civil = input("ingrese estado civil (S = soltero, C = casado):")
recidencia = input("vive en campo o cuidad (U = urbano, R = rural):")
edad = 2022 - nacimiento 
if (anos > 10) and (hijos >= 2):
  print("APROBADO")
elif (estado_civil == "C") and (hijos > 3) and (edad > 45) or (edad < 55):
  print("APROBADO")
elif (ingresos > 2500000) and (estado_civil == "S") and (recidencia == "U"):
  print("APROBADO")
elif (ingresos > 3500000) and (anos > 5):
  print("APROBADO")
elif (recidencia == "R") and (estado_civil == "C") and (hijos < 2):
  print("APROBADO")
else: 
  print("RECHAZADO")