def calcular_aprobacion_credito():
    ingreso = float(input("Ingrese su ingreso en pesos: "))
    ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
    num_hijos = int(input("Ingrese el número de hijos: "))
    anos_banco = int(input("Ingrese los años de pertenencia al banco: "))
    estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
    ubicacion = input("Ingrese su ubicación (U para urbano, R para rural): ")

    if anos_banco > 10 and num_hijos >= 2:
        return "APROBADO"
    elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - ano_nacimiento) <= 55:
        return "APROBADO"
    elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return "APROBADO"
    elif ingreso > 3500000 and anos_banco > 5:
        return "APROBADO"
    elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return "APROBADO"
    else:
        return "RECHAZADO"


resultado = calcular_aprobacion_credito()
print("Estado de la solicitud: " + resultado)
