#Aprobación de créditos
def aprobar_credito(ingreso, anno_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion):
    # Regla 1: Pertenencia al banco y número de hijos
    if anos_pertenencia > 10 and num_hijos >= 2:
        return True

    # Regla 2: Estado civil, número de hijos y edad
    if estado_civil == 'C' and num_hijos > 3 and 45 <= (2023 - anno_nacimiento) <= 55:
        return True

    # Regla 3: Ingresos, estado civil y ubicación
    if ingreso > 2500000 and estado_civil == 'S' and ubicacion == 'U':
        return True

    # Regla 4: Ingresos y pertenencia al banco
    if ingreso > 3500000 and anos_pertenencia > 5:
        return True

    # Regla 5: Ubicación, estado civil y número de hijos
    if ubicacion == 'R' and estado_civil == 'C' and num_hijos < 2:
        return True

    # Ninguna regla se cumple, crédito rechazado
    return False

# Solicitar al cliente ingresar sus datos
ingreso = int(input("Ingrese su ingreso en pesos: "))
anno_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anos_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese su ubicación (U para urbano, R para rural): ")

# Verificar si el crédito es aprobado o rechazado
if aprobar_credito(ingreso, anno_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion):
    print("APROBADO")
else:
    print("RECHAZADO")
