# Solicitar los datos del cliente
ingreso = int(input("Ingrese el ingreso mensual (en pesos): "))
ano_nacimiento = int(input("Ingrese el año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anos_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese el estado civil (S para soltero, C para casado): ")
lugar_residencia = input("Ingrese el lugar de residencia (U para urbano, R para rural): ")

# Verificar las reglas para la aprobación del crédito
aprobado = False

if anos_pertenencia > 10 and num_hijos >= 2:
    aprobado = True

elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - ano_nacimiento) <= 55:
    aprobado = True

elif ingreso > 2500000 and estado_civil == "S" and lugar_residencia == "U":
    aprobado = True

elif ingreso > 3500000 and anos_pertenencia > 5:
    aprobado = True

elif lugar_residencia == "R" and estado_civil == "C" and num_hijos < 2:
    aprobado = True

# Imprimir el resultado de la aprobación del crédito
if aprobado:
    print("APROBADO")
else:
    print("RECHAZADO")
