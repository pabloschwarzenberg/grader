#Aprobación de créditos
def aprobar_credito(ingreso, anio_nacimiento, num_hijos, anios_banco, estado_civil, ubicacion):
    # Regla 1: Más de 10 años en el banco y dos o más hijos
    if anios_banco > 10 and num_hijos >= 2:
        return "APROBADO"

    # Regla 2: Casado, más de tres hijos y edad entre 45 y 55 años
    if estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - anio_nacimiento) <= 55:
        return "APROBADO"

    # Regla 3: Ingresos superiores a $2,500,000, soltero y vive en la ciudad
    if ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return "APROBADO"

    # Regla 4: Ingresos superiores a $3,500,000 y más de 5 años en el banco
    if ingreso > 3500000 and anios_banco > 5:
        return "APROBADO"

    # Regla 5: Vive en el campo, casado y menos de dos hijos
    if ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return "APROBADO"

    # Si ninguna de las reglas anteriores se cumple, se rechaza el crédito
    return "RECHAZADO"


# Solicitar al cliente que ingrese sus datos
ingreso = int(input("Ingrese su ingreso mensual en pesos: "))
anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos que tiene: "))
anios_banco = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese su ubicación (U para urbano, R para rural): ")

# Llamar a la función para determinar si se aprueba o se rechaza el crédito
resultado = aprobar_credito(ingreso, anio_nacimiento, num_hijos, anios_banco, estado_civil, ubicacion)

# Imprimir el resultado en pantalla
print("Resultado:", resultado)
      