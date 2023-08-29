def aprobar_credito(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion):
    if anos_pertenencia > 10 and num_hijos >= 2:
        return True

    if estado_civil == "C" and num_hijos > 3 and ano_nacimiento >= 45 and ano_nacimiento <= 55:
        return True

    if ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return True

    if ingreso > 3500000 and anos_pertenencia > 5:
        return True

    if ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return True

    return False

# Solicitar al usuario los datos necesarios
ingreso = int(input("Ingrese el ingreso en pesos: "))
ano_nacimiento = int(input("Ingrese el año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anos_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese el estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese la ubicación (U para urbano, R para rural): ")

# Determinar si se aprueba o rechaza el crédito utilizando la función aprobar_credito
if aprobar_credito(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion):
    print("APROBADO")
else:
    print("RECHAZADO")
