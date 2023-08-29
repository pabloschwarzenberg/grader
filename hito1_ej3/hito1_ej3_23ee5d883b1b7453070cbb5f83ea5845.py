#Aprobación de créditos
def verificar_aprobacion_credito():
    ingreso = int(input("Ingrese su ingreso en pesos: "))
    ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
    num_hijos = int(input("Ingrese el número de hijos: "))
    anos_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
    estado_civil = input("Ingrese su estado civil (S - Soltero, C - Casado): ")
    tipo_vivienda = input("Ingrese el tipo de vivienda (U - Urbano, R - Rural): ")

    if anos_pertenencia > 10 and num_hijos >= 2:
        return "APROBADO"

    if estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - ano_nacimiento) <= 55:
        return "APROBADO"

    if ingreso > 2500000 and estado_civil == "S" and tipo_vivienda == "U":
        return "APROBADO"

    if ingreso > 3500000 and anos_pertenencia > 5:
        return "APROBADO"

    if tipo_vivienda == "R" and estado_civil == "C" and num_hijos < 2:
        return "APROBADO"

    return "RECHAZADO"

resultado = verificar_aprobacion_credito()
print(resultado)