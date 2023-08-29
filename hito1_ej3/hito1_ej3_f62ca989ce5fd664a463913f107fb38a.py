#Aprobación de créditos
ingreso = int(input("Ingrese el monto de sus ingresos:$ "))
a_nacimiento = int(input("Ingrese su fecha de nacimiento: "))
edad = 2022 - a_nacimiento
numero_hijos = int(input("Ingrese cuantos hijos tiene: "))
a_antiguedad = int(input("Ingrese años de antiguedad en el banco: "))
estado_civil = input("Ingrese estado civil: ")
lugar_donde_vive = input("Ingrese lugar donde recide: ")

if a_antiguedad >=10 and numero_hijos >=2:
  print("APROBADO")
elif estado_civil == "C" and numero_hijos > 3 and edad >= 45 and edad <= 55:
  print("APROBADO")
elif ingreso >2500000 and estado_civil == "S" and lugar_donde_vive == "U":
  print("APROBADO")
elif ingreso > 3500000 and a_antiguedad > 5:
  print("APROBADO")
elif lugar_donde_vive == "R"  and estado_civil == "C" and numero_hijos <2:
  print("APROBADO")
else:
  print("RECHAZADO")