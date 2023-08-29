#Aprobación de créditos
# Pedir los datos al cliente
ingreso = int(input("Ingrese su ingreso mensual en pesos: "))
anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos que tiene: "))
anios_pertenencia = int(input("Ingrese el número de años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
lugar_residencia = input("Ingrese si vive en campo (R para rural) o ciudad (U para urbano): ")

# Verificar las reglas de aprobación
aprobado = False

if anios_pertenencia > 10 and num_hijos >= 2:
    aprobado = True

if estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - anio_nacimiento) <= 55:
    aprobado = True

if ingreso > 2500000 and estado_civil == "S" and lugar_residencia == "U":
    aprobado = True

if ingreso > 3500000 and anios_pertenencia > 5:
    aprobado = True

if lugar_residencia == "R" and estado_civil == "C" and num_hijos < 2:
    aprobado = True

# Imprimir el resultado
if aprobado:
    print("APROBADO")
else:
    print("RECHAZADO")
      