#Aprobación de créditos
def evaluar_credito():
    ingreso = float(input("Ingrese su ingreso en pesos: "))
    anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
    num_hijos = int(input("Ingrese el número de hijos: "))
    anios_banco = int(input("Ingrese los años de pertenencia al banco: "))
    estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
    ubicacion = input("Ingrese su ubicación (U para urbano, R para rural): ")

    if anios_banco > 10 and num_hijos >= 2:
        return True

    if estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - anio_nacimiento) <= 55:
        return True

    if ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return True

    if ingreso > 3500000 and anios_banco > 5:
        return True

    if ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return True

    return False

if evaluar_credito():
    print("APROBADO")
else:
    print("RECHAZADO")
   