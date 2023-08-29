#Aprobación de créditos
ingresos = eval(input("ingrese la cantidad de ingresos en pesos: "))
año_de_nacimiento = eval(input("ingrese su año de nacimiento: "))
numero_de_hijos = eval(input("ingrese la cantidad de hijos que tenga: "))
años_pertenecientes_del_banco = eval(input("ingrese la cantidad de años pertenecientes al banco: "))
estado_civil = str(input("ingrese su estado civil, si es soltero ponga una (S mayuscula) o una (C mayuscula)si es casado:  "))
campo_ciudad = str(input("ingrese una letra (U mayuscula) si vive en la ciudad o ingrese una letra(R mayuscula) si vive en el campo: "))
edad = (2020) - (año_de_nacimiento)

if (años_pertenecientes_del_banco > 10) and (numero_de_hijos >= 2):
  print("APROBADO")
elif (estado_civil == "C") and (numero_de_hijos > 3) and (edad >= 45 and edad <= 55):
  print("APROBADO")
elif (ingresos > 2500000) and (estado_civil == "S") and (campo_ciudad == "U"):
  print("APROBADO")
elif (ingresos > 3500000) and (años_pertenecientes_del_banco > 5):
  print("APROBADO")
elif (campo_ciudad == "R") and (estado_civil == "C") and (numero_de_hijos < 2):
  print("APROBADO")
else:
  print("RECHAZADO")