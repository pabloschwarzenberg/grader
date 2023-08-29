#Aprobación de créditos
def aprobar_credito(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, lugar_residencia):
    if anos_pertenencia > 10 and num_hijos >= 2:
        return True
    elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - ano_nacimiento) <= 55:
        return True
    elif ingreso > 2500000 and estado_civil == "S" and lugar_residencia == "U":
        return True
    elif ingreso > 3500000 and anos_pertenencia > 5:
        return True
    elif lugar_residencia == "R" and estado_civil == "C" and num_hijos < 2:
        return True
    else:
        return False

# Pedir al cliente que ingrese sus datos
ingreso = int(input("Ingrese su ingreso en pesos: "))
ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anos_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
lugar_residencia = input("Ingrese si vive en campo (R) o ciudad (U): ")

# Determinar si el crédito es aprobado o rechazado
if aprobar_credito(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, lugar_residencia):
    print("APROBADO")
else:
    print("RECHAZADO")