ingreso_pesos = int(input("Ingrese su ingreso mensual en pesos: "))
Año_nacimiento = int(input("Ingrese su año de nacimiento: "))
N_hijos = int(input("Ingrese el número de hijos: "))
años_pertenenciaB = int(input("Ingrese la cantidad de años de pertenencia al banco: "))
Su_estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese su ubicación (U para urbano, R para rural): ")

def verificar_aprobacion(ingreso_pesos, Año_nacimiento, N_hijos, años_pertenenciaB, Su_estado_civil, ubicacion):
    if años_pertenenciaB > 10 and N_hijos >= 2:
        return True
    if Su_estado_civil == "C" and N_hijos > 3 and 45 <= (2023 - Año_nacimiento) <= 55:
        return True
    if ingreso_pesos > 2500000 and Su_estado_civil == "S" and ubicacion == "U":
        return True
    if ingreso_pesos > 3500000 and años_pertenenciaB > 5:
        return True
    if ubicacion == "R" and Su_estado_civil == "C" and N_hijos < 2:
        return True
    return False

aprobado = verificar_aprobacion(ingreso_pesos, Año_nacimiento, N_hijos, años_pertenenciaB, Su_estado_civil, ubicacion)

# Imprimir resultado
if aprobado:
    print("APROBADO")
else:
    print("RECHAZADO")
        