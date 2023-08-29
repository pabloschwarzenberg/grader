def aprobar_credito(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion):
    if anos_pertenencia > 10 and num_hijos >= 2:
        return "APROBADO"  # Regla 1: Más de 10 años en el banco y dos o más hijos
    elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - ano_nacimiento) <= 55:
        return "APROBADO"  # Regla 2: Casado, más de tres hijos y edad entre 45 y 55 años
    elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return "APROBADO"  # Regla 3: Ingresos superiores a $2.500.000, soltero y vive en la ciudad
    elif ingreso > 3500000 and anos_pertenencia > 5:
        return "APROBADO"  # Regla 4: Ingresos superiores a $3.500.000 y más de 5 años en el banco
    elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return "APROBADO"  # Regla 5: Vive en el campo, casado y menos de dos hijos
    else:
        return "RECHAZADO"  # No cumple ninguna regla, crédito rechazado


# Solicitar al cliente que ingrese sus datos
ingreso = int(input("Ingrese su ingreso mensual (en pesos): "))
ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos que tiene: "))
anos_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese su ubicación (U para urbano, R para rural): ")

# Determinar si se aprueba el crédito
decision = aprobar_credito(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion)

# Imprimir la decisión
print(decision)

      