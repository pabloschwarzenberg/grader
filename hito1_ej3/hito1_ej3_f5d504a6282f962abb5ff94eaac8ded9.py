#Aprobación de créditos
  # Solicitar datos al cliente
ingreso = int(input("Ingrese su ingreso en pesos: "))
anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos que tiene: "))
anos_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese su ubicación (U para urbano, R para rural): ")

# Verificar las condiciones para la aprobación del crédito
aprobado = False

if anos_pertenencia > 10 and num_hijos >= 2:
    aprobado = True

if estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - anio_nacimiento) <= 55:
    aprobado = True

if ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
    aprobado = True

if ingreso > 3500000 and anos_pertenencia > 5:
    aprobado = True

if ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
    aprobado = True

# Imprimir el resultado
if aprobado:
    print("APROBADO")
else:
    print("RECHAZADO")
