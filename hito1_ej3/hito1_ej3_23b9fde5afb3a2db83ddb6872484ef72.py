#Aprobación de créditos
ingreso = eval(input("Escriba sus ingresos: $"))
año_nacimiento = eval(input("Escriba su año de nacimiento: "))
hijos = eval(input("Escriba el número de hijos que tiene: "))
años_banco = eval(input("Escriba el número de años que lleve en el banco: "))
estado_civil = input("Estado civil ('S' si es soltero o 'C' si es casado: ")
donde_vive = input("¿Vive en campo o ciudad? ('U' si es en la ciudad o 'R' si es en el campo): ")

if (años_banco > 10 and hijos >= 2):
  print("APROBADO")
elif (estado_civil == "C" or "c" and hijos > 3 and año_nacimiento >= 1966 or año_nacimiento <= 1976):
  print("APROBADO")
elif (ingreso > 2500000 and estado_civil == "S" or "s" and donde_vive == "U" or "u"):
  print("APROBADO")
elif (ingreso > 3500000 and años_banco > 5):
  print("APROBADO")
elif (donde_vive == "R" or "r" and estado_civil == "C" or "c" and hijos < 2):
  print("APROBADO")
else:
  print("RECHAZADO")     