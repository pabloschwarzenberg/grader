#Aprobación de créditos
ingresos = int(input("Ingrese el monto de ingreso en pesos: "))
año_nacimiento = int(input("Ingrese su año de nacimiento: "))
edad = 2023 - año_nacimiento
hijos = int(input("Indique la cantidad de hijos que tiene: "))
año_banco = int(input("Indique la cantidad de años de perctenencia en este banco: "))
estado_civil = input("Indique su estado civil (S: soltero, C: casado)")
campo_ciudad = input("Indique si vive en campo o cuidad (U: urbano, R: rural)")

if año_banco > 10 and hijos >= 2:
  print("APROBADO")

elif estado_civil == "C" and hijos > 3 and 45 < edad < 55:
  print("APROBADO")

elif ingresos > 2500000 and estado_civil == "S" and campo_ciudad == "U":
  print("APROBADO")

elif ingresos > 3500000 and año_banco > 5:
  print("APROBADO")

elif campo_ciudad == "R" and estado_civil == "C" and hijos < 2:
  print("APROBADO")

else:
  print("RECHAZADO")    