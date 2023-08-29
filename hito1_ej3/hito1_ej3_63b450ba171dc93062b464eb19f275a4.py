#Aprobación de créditos
ingreso = int(input("Entregue su ingreso: "))
anyo_nacimiento = int(input("Ingrese su año de nacimiento: "))
numero_hijos = int(input("Ingrese su número de hijos: "))
anyos_pertenencia_banco = int(input("Ingrese sus años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil: ")
tipo_vivienda =  input("Ingrese si vive en el campo o ciudad: ")
edad = 2022 - anyo_nacimiento

if anyos_pertenencia_banco > 10 and numero_hijos >= 2:
  print("APROBADO")
elif estado_civil == "C" and numero_hijos >= 3 and edad > 45 and edad < 55:
  print("APROBADO")
elif ingreso > 2500000 and estado_civil == "S" and tipo_vivienda == "U":
  print("APROBADO")
elif ingreso > 3500000 and anyos_pertenencia_banco > 5:
  print("APROBADO")
elif tipo_vivienda == "R" and estado_civil == "C" and numero_hijos < 2:
  print("APROBADO")
else:
  print("RECHAZADO")
