# Solicitar al cliente la información requerida
ingreso = int(input("Ingrese su ingreso en pesos: "))
anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el numero de hijos: "))
anios_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese su ubicacion (U para urbano, R para rural): ")

# Verificar las reglas para decidir la aprobación del credito
aprobado = False

if anios_pertenencia > 10 and num_hijos >= 2:
    aprobado = True

if estado_civil == "C" and num_hijos > 3 and anio_nacimiento >= 45 and anio_nacimiento <= 55:
    aprobado = True

if ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
    aprobado = True

if ingreso > 3500000 and anios_pertenencia > 5:
    aprobado = True

if ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
    aprobado = True

# Imprimir el resultado (APROBADO o RECHAZADO)
if aprobado:
    print("APROBADO")
else:
    print("RECHAZADO")