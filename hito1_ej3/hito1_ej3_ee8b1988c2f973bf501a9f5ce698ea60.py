#Aprobación de créditos
      # Solicitar información al cliente
ingreso = float(input("Ingrese el ingreso mensual en pesos: "))
ano_nacimiento = int(input("Ingrese el año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anos_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese el estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese la ubicación (U para urbano, R para rural): ")

# Verificar las condiciones para aprobar o rechazar el crédito
if anos_pertenencia > 10 and num_hijos >= 2:
    # Aprobar el crédito si el cliente pertenece más de 10 años al banco y tiene dos o más hijos
    resultado = "APROBADO"
elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - ano_nacimiento) <= 55:
    # Aprobar el crédito si el cliente es casado, tiene más de tres hijos y tiene entre 45 y 55 años
    resultado = "APROBADO"
elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
    # Aprobar el crédito si el cliente tiene ingresos superiores a $2.500.000, es soltero y vive en la ciudad
    resultado = "APROBADO"
elif ingreso > 3500000 and anos_pertenencia > 5:
    # Aprobar el crédito si el cliente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
    resultado = "APROBADO"
elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
    # Aprobar el crédito si el cliente vive en el campo, es casado y tiene menos de dos hijos
    resultado = "APROBADO"
else:
    # Rechazar el crédito en los demás casos
    resultado = "RECHAZADO"

# Imprimir el resultado
print("Resultado:", resultado)
