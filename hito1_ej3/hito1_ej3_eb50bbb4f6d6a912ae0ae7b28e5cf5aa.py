#Aprobación de créditos
#Aprobación de créditos
ingresos = int(input("ingresos: "))
nacimiento = int(input("año de nacimiento: "))
hijos = int(input("numero de hijos: "))
años_banco = int(input("años en el banco: "))
estado_civil = str(input("estado civil: ")) #S = soltero, C = casado
vivencia = str(input("vive en campo o ciudad: ")) #U = urbano(ciudad), R = rural(campo)
edad = 2022 - nacimiento

if años_banco > 10 or hijos > 2 :
  print("APROBADO")

elif estado_civil == "C" or hijos > 3 or edad >= 45 and edad <= 55 :
  print("APROBADO")

elif ingresos >= 2500000 or estado_civil == "S" or vivencia == "U" :
  print("APROBADO")

elif ingresos >= 3500000 or años_banco > 5 :
  print("APROBADO")

elif vivencia == "R" or estado_civil == "C" or hijos < 2 :
  print("APROBADO")

else :
  print("RECHAZADO")