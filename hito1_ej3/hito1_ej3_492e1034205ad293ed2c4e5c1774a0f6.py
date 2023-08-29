def aprobar_credito(ingreso, año_nacimiento, num_hijos, años_pertenencia, estado_civil, lugar_residencia):
    if años_pertenencia > 10 and num_hijos >= 2:
        return True
    elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - año_nacimiento) <= 55:
        return True
    elif ingreso > 2500000 and estado_civil == "S" and lugar_residencia == "U":
        return True
    elif ingreso > 3500000 and años_pertenencia > 5:
        return True
    elif lugar_residencia == "R" and estado_civil == "C" and num_hijos < 2:
        return True
    else:
        return False

# Solicitar los datos al cliente
ingreso = int(input("Ingrese el ingreso mensual en pesos: "))
año_nacimiento = int(input("Ingrese el año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
años_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese el estado civil (S para soltero, C para casado): ")
lugar_residencia = input("Ingrese el lugar de residencia (U para urbano, R para rural): ")

# Verificar si se aprueba o rechaza el crédito
if aprobar_credito(ingreso, año_nacimiento, num_hijos, años_pertenencia, estado_civil, lugar_residencia):
    print("APROBADO")
else:
    print("RECHAZADO")