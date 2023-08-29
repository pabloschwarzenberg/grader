def solicitar_datos():
    ingreso = float(input("Ingresa tu ingreso mensual en pesos: "))
    dia_de_nacimiento = int(input("Ingresa tu dia de nacimiento: "))
    num_hijos = int(input("Ingresa el numero de hijos que tienes: "))
    tiempo_en_el_banco = int(input("Ingresa el tiempo que llevas en el banco: "))
    estado_civil = input("Ingresa tu estado civil (S para soltero, C para casado): ")
    ubicacion = input("Ingresa tu ubicacion (U para urbano, R para rural): ")
    return ingreso, dia_de_nacimiento, num_hijos, tiempo_en_el_banco, estado_civil, ubicacion

def aprobar_credito(ingreso, dia_de_nacimiento, num_hijos, tiempo_en_el_banco, estado_civil, ubicacion):
    if tiempo_en_el_banco > 10 and num_hijos >= 2:
        return True
    elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - dia_de_nacimiento) <= 55:
        return True
    elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return True
    elif ingreso > 3500000 and tiempo_en_el_banco > 5:
        return True
    elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return True
    else:
        return False

ingreso, dia_de_nacimiento, num_hijos, tiempo_en_el_banco, estado_civil, ubicacion = solicitar_datos()

if aprobar_credito(ingreso, dia_de_nacimiento, num_hijos, tiempo_en_el_banco, estado_civil, ubicacion):
    print("APROBADO")
else:
    print("RECHAZADO")