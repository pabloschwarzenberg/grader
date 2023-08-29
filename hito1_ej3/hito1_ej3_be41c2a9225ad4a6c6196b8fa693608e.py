#Aprobación de créditos
def solicitar_datos():
    ingreso = float(input("Ingrese su ingreso mensual en pesos: "))
    a_nacimiento = int(input("Ingrese su año de nacimiento: "))
    num_hijos = int(input("Ingrese el número de hijos que tiene: "))
    a_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
    estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
    tipo_vivienda = input("Ingrese el tipo de vivienda (U para urbano, R para rural): ")
    return ingreso, a_nacimiento, num_hijos, a_pertenencia, estado_civil, tipo_vivienda

def aprobar_credito(ingreso, a_nacimiento, num_hijos, a_pertenencia, estado_civil, tipo_vivienda):
    if a_pertenencia > 10 and num_hijos >= 2:
        return True
    if estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - a_nacimiento) <= 55:
        return True
    if ingreso > 2500000 and estado_civil == "S" and tipo_vivienda == "U":
        return True
    if ingreso > 3500000 and a_pertenencia > 5:
        return True
    if tipo_vivienda == "R" and estado_civil == "C" and num_hijos < 2:
        return True
    return False

# Solicitar datos al cliente
ingreso, a_nacimiento, num_hijos, a_pertenencia, estado_civil, tipo_vivienda = solicitar_datos()

# Verificar si se aprueba el crédito
if aprobar_credito(ingreso, a_nacimiento, num_hijos, a_pertenencia, estado_civil, tipo_vivienda):
    print("APROBADO")
else:
    print("RECHAZADO")
      