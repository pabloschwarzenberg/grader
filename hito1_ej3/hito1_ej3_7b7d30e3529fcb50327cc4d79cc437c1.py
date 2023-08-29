#Aprobación de créditos
def aprobar_credito(ingreso, anio_nacimiento, num_hijos, anios_pertenencia, estado_civil, ubicacion):
    if anios_pertenencia > 10 and num_hijos >= 2:
        return "APROBADO"  # Regla 1
    elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - anio_nacimiento) <= 55:
        return "APROBADO"  # Regla 2
    elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return "APROBADO"  # Regla 3
    elif ingreso > 3500000 and anios_pertenencia > 5:
        return "APROBADO"  # Regla 4
    elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return "APROBADO"  # Regla 5
    else:
        return "RECHAZADO"  # No se cumple ninguna regla de aprobación

# Solicitar los datos al cliente
ingreso = int(input("Ingrese el ingreso mensual en pesos: "))
anio_nacimiento = int(input("Ingrese el año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anios_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese el estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese la ubicación (U para urbano, R para rural): ")

# Verificar si se aprueba el crédito
resultado = aprobar_credito(ingreso, anio_nacimiento, num_hijos, anios_pertenencia, estado_civil, ubicacion)

# Imprimir el resultado
print("Resultado:", resultado) 
 