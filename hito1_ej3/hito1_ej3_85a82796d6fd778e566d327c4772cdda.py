#Aprobación de créditos
def aprobar_credito(ingreso, anio_nacimiento, num_hijos, anios_pertenencia, estado_civil, ubicacion):
    if anios_pertenencia > 10 and num_hijos >= 2:
        return "APROBADO"  # Regla 1

    if estado_civil == "C" and num_hijos > 3 and anio_nacimiento >= 45 and anio_nacimiento <= 55:
        return "APROBADO"  # Regla 2

    if ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return "APROBADO"  # Regla 3

    if ingreso > 3500000 and anios_pertenencia > 5:
        return "APROBADO"  # Regla 4

    if ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return "APROBADO"  # Regla 5

    return "RECHAZADO"  # Ninguna regla se cumple


# Solicitar los datos al cliente
ingreso = int(input("Ingrese su ingreso en pesos: "))
anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anios_pertenencia = int(input("Ingrese el número de años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese su ubicación (U para urbano, R para rural): ")

# Determinar si se aprueba o rechaza el crédito
resultado = aprobar_credito(ingreso, anio_nacimiento, num_hijos, anios_pertenencia, estado_civil, ubicacion)

# Imprimir el resultado
print("Resultado:", resultado)
      