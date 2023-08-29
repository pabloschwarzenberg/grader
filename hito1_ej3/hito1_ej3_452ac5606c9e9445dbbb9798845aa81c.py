# Aprobación de créditos
# Obtener los datos del cliente
ingreso = float(input("Ingrese el ingreso mensual (en pesos): "))
anio_nacimiento = int(input("Ingrese el año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anios_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese el estado civil (S: soltero, C: casado): ")
ubicacion = input("Ingrese la ubicación (U: urbano, R: rural): ")

# Verificar si se aprueba el crédito
aprobado = False

if anios_pertenencia > 10 and num_hijos >= 2:
    aprobado = True
elif estado_civil == "C" and num_hijos > 3 and anio_nacimiento >= 45 and anio_nacimiento <= 55:
    aprobado = True
elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
    aprobado = True
elif ingreso > 3500000 and anios_pertenencia > 5:
    aprobado = True
elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
    aprobado = True

# Imprimir el resultado
if aprobado:
    print("APROBADO")
else:
    print("RECHAZADO")