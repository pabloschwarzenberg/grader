def aprobar_credito():
    ingreso = float(input("Por favor, ingrese su ingreso en pesos: "))
    ano_nacimiento = int(input("Por favor, ingrese su año de nacimiento: "))
    num_hijos = int(input("Por favor, ingrese el número de hijos que tiene: "))
    anos_pertenencia = int(input("Por favor, ingrese los años que ha sido cliente del banco: "))
    estado_civil = input("Por favor, ingrese su estado civil (S para soltero, C para casado): ")
    ubicacion = input("Por favor, ingrese su ubicación (U para urbano, R para rural): ")

    if anos_pertenencia > 10 and num_hijos >= 2:
        return "APROBADO"

    if estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - ano_nacimiento) <= 55:
        return "APROBADO"

    if ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return "APROBADO"

    if ingreso > 3500000 and anos_pertenencia > 5:
        return "APROBADO"

    if ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return "APROBADO"

    return "RECHAZADO"

resultado = aprobar_credito()
print(resultado)
