#Aprobación de créditos

print("Bievenido al banco.")
print("Para solicitar un credito, ingrese los siguientes datos.")

ingresos = int(input("Cuales son sus ingresos en pesos: $"))
anio_de_nacimiento = int(input("En que año nacio: "))
numero_de_hijos = int(input("Ingrese la cantidad de hijos que tiene: "))
anios_de_pertenencia_banco = int(input("Ingrese la cantidad de años que es cliente del banco: "))
estado_civil = input("Ingrese su estado civil, como 'S', para soltero y 'C', para casado: ")
vivienda = input("Ingrese donde vive 'U', para ciudad y 'R', para Campo: ")
edad = 2022 - anio_de_nacimiento

#condiciones

if anios_de_pertenencia_banco > 10 and numero_de_hijos >=2:
  print("APROBADO")

elif estado_civil == "C" and numero_de_hijos > 3 and edad >= 45 and edad <=55:
  print("APROBADO")

elif ingresos >= 2500000 and estado_civil == "S" and vivienda == "U":
  print("APROBADO")

elif ingresos >= 3500000 and anios_de_pertenencia_banco > 5:
  print("APROBADO")

elif vivienda == "R" and estado_civil == "C" and numero_de_hijos < 2:
  print("APROBADO")

else: 
  print("RECHAZADO")