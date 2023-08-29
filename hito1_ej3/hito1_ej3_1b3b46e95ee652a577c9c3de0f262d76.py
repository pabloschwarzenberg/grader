#Aprobación de créditos
inrgesos = int(input("ingrese sus ingreson en CLP"))
ano_nacimiento = int(input("ingrese su año de nacimiento"))
n_hijos = int(input("ingrese el numero de hijos/as que tine"))
pertenencia_banco = int(input("ingrese su año de pertenecia albanco"))
estado_civil = input("s: soltero  c: casado")
hubicacion = input("u: urbano  r: rural")

edad = 2021-ano_nacimiento
if (pertenencia_banco >= 10) and (n_hijos >= 2):
  print("  APROBADO  ")
elif (estado_civil == "c" or estado_civil =="C") and (n_hijos >= 3) and (edad >= 45) and (edad <= 55):
  print("  APROBADO  ")
elif (inrgesos >= 2500000) and (estado_civil == "s" or estado_civil == "S") and (hubicacion == "u" or hubicacion == "U"):
  print("  RECHAZADO  ")
elif(inrgesos >= 3500000) and (pertenencia_banco >= 5):
  print("  RECHAZADO  ")
elif (hubicacion == "r" or hubicacion == "R") and (estado_civil == "c" or estado_civil == "C") and (n_hijos <= 2):
  print("  APROBADO  ")