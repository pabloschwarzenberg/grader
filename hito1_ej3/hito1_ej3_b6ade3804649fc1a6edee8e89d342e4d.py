#Aprobación de créditos

ingreso = int(input("Ingrese su ingreso en pesos: "))
ano_de_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_de_hijos = int(input("Ingrese el número de hijos: "))
anos_de_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese su ubicación (U para urbano, R para rural): ")

if anos_de_pertenencia > 10 and num_de_hijos >= 2:
    resultado = "APROBADO"
elif estado_civil == "C" and num_de_hijos > 3 and 45 <= (2023 - ano_de_nacimiento) <= 55:
    resultado = "APROBADO"
elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
    resultado = "APROBADO"
elif ingreso > 3500000 and anos_de_pertenencia > 5:
    resultado = "APROBADO"
elif ubicacion == "R" and estado_civil == "C" and num_de_hijos < 2:
    resultado = "APROBADO"
else:
    resultado = "RECHAZADO"

print("El resultado de la solicitud de crédito es:", resultado)
