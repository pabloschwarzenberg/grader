#Aprobación de créditos
def aprobar_credito(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion):
    if anos_pertenencia > 10 and num_hijos >= 2:
        return True

    if estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - ano_nacimiento) <= 55:
        return True

    if ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return True

    if ingreso > 3500000 and anos_pertenencia > 5:
        return True

    if ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return True

    return False

# Ejemplo de uso
ingreso = 3000000
ano_nacimiento = 1980
num_hijos = 2
anos_pertenencia = 12
estado_civil = "C"
ubicacion = "R"

if aprobar_credito(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion):
    print("Crédito aprobado")
else:
    print("Crédito rechazado")
      