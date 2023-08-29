#Aprobación de créditos
      # Obtener los datos del cliente
ingreso = int(input("Ingrese el ingreso mensual del cliente en pesos: "))
ano_nacimiento = int(input("Ingrese el año de nacimiento del cliente: "))
num_hijos = int(input("Ingrese el número de hijos del cliente: "))
anos_pertenencia = int(input("Ingrese los años de pertenencia al banco del cliente: "))
estado_civil = input("Ingrese el estado civil del cliente (S para soltero, C para casado): ")
ubicacion = input("Ingrese la ubicación del cliente (U para urbano, R para rural): ")

# Verificar las reglas para aprobar o rechazar el crédito
if anos_pertenencia > 10 and num_hijos >= 2:
    print("APROBADO")
elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - ano_nacimiento) <= 55:
    print("APROBADO")
elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
    print("APROBADO")
elif ingreso > 3500000 and anos_pertenencia > 5:
    print("APROBADO")
elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
