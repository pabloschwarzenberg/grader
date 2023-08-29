print("Bienvenido al banco, por favor sea sincero al ingresar sus datos")

ingreso = int(input("Introduzca sus ingresos: "))
año = int(input("Introduzca su año de nacimiento: "))
edad = 2022 - año
hijos = int(input("Ingrese cuantos hijos tiene: "))
años_banco = int(input("Ingrese cuantos años lleva perteneciendo nnuestro banco: "))
estado = str(input("Ingrese su estado civil, S: soltero, C, casado: "))
vivienda = str(input("Indique el sector en donde vive U: urbano, R: rural: "))

if años_banco>=10 and hijos>=2:
  print("APROBADO")
elif estado == "C" or estado == "casado" and hijos>=3 and edad>=45 and hijos<=55:
  print("APROBADO") 
elif ingreso>=2500000 and estado == "S" or estado == "soltero" and vivienda == "U" or vivienda == "urbano":
  print("APROBADO")
elif ingreso>=3500000 and años_banco>=5:
  print("APROBADO")
elif vivienda == "R" or vivienda == "rural" and hijos<=2 and estado == "C" or estado == "casado":
  print("APROBADO")
else:
  print("RECHAZADO")
