#Aprobación de créditos
def aprobar_credito(ingreso, nacimiento, hijos, anios_banco, estado_civil, ubicacion):
    # Regla 1: Pertenece más de 10 años al banco y tiene dos o más hijos
    if anios_banco > 10 and hijos >= 2:
        return "APROBADO"

    # Regla 2: Casado, más de tres hijos y entre 45 y 55 años
    if estado_civil == "C" and hijos > 3 and nacimiento >= 1968 and nacimiento <= 1978:
        return "APROBADO"

    # Regla 3: Ingresos superiores a $2.500.000, soltero y vive en la ciudad
    if ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return "APROBADO"

    # Regla 4: Ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
    if ingreso > 3500000 and anios_banco > 5:
        return "APROBADO"

    # Regla 5: Vive en el campo, es casado y tiene menos de dos hijos
    if ubicacion == "R" and estado_civil == "C" and hijos < 2:
        return "APROBADO"

    # Si no se cumple ninguna regla, se rechaza el crédito
    return "RECHAZADO"

# Solicitar al cliente los datos requeridos
ingreso = int(input("Ingrese el ingreso mensual en pesos: "))
nacimiento = int(input("Ingrese el año de nacimiento: "))
hijos = int(input("Ingrese el número de hijos: "))
anios_banco = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese el estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese la ubicación (U para urbano, R para rural): ")

# Obtener el resultado de la aprobación del crédito
resultado = aprobar_credito(ingreso, nacimiento, hijos, anios_banco, estado_civil, ubicacion)

# Imprimir el resultado
print("Resultado:", resultado)
      