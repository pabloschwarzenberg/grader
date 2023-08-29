    # Función para obtener la edad a partir del año de nacimiento
def obtener_edad(ano_nacimiento):
    ano_actual = 2023  # Asumiendo que el año actual es 2023
    return ano_actual - ano_nacimiento

# Función para obtener la decisión de aprobación del crédito
def obtener_decision_aprobacion(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion):
    edad = obtener_edad(ano_nacimiento)

    if anos_pertenencia > 10 and num_hijos >= 2:
        return "APROBADO"

    if estado_civil == "C" and num_hijos > 3 and edad >= 45 and edad <= 55:
        return "APROBADO"

    if ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return "APROBADO"

    if ingreso > 3500000 and anos_pertenencia > 5:
        return "APROBADO"

    if ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return "APROBADO"

    return "RECHAZADO"

# Obtener los datos del cliente
ingreso = float(input("Ingrese el ingreso del cliente en pesos: "))
ano_nacimiento = int(input("Ingrese el año de nacimiento del cliente: "))
num_hijos = int(input("Ingrese el número de hijos del cliente: "))
anos_pertenencia = int(input("Ingrese los años de pertenencia al banco del cliente: "))
estado_civil = input("Ingrese el estado civil del cliente ('S' para soltero, 'C' para casado): ")
ubicacion = input("Ingrese la ubicación del cliente ('U' para urbano, 'R' para rural): ")

# Obtener la decisión de aprobación
decision = obtener_decision_aprobacion(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion)

# Imprimir el mensaje de aprobación o rechazo
if decision == "APROBADO":
    print("Crédito APROBADO")
else:
    print("Crédito RECHAZADO")
 