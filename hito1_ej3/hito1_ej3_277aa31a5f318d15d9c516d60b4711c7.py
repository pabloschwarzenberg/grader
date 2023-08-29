import random

def verificar_aprobacion(ingreso, año_nacimiento, num_hijos, años_pertenencia, estado_civil, ubicacion):
    if años_pertenencia > 10 and num_hijos >= 2:
        return True

    if estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - año_nacimiento) <= 55:
        return True

    if ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return True

    if ingreso > 3500000 and años_pertenencia > 5:
        return True

    if ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return True

    return False


def obtener_respuesta_aleatoria(respuestas):
    return random.choice(respuestas)


respuestas_aprobado = ["APROBADO"]

respuestas_rechazado = ["RECHAZADO"]

ingreso = float(input(" Por favor, indiqueme su ingreso mensual en pesos: "))
año_nacimiento = int(input("necesito saber su año de nacimiento: "))
num_hijos = int(input("Cuántos hijos tiene? "))
años_pertenencia = int(input("Hace cuántos años es cliente de nuestro banco? "))
estado_civil = input("Por favor, ingrese su estado civil (S para soltero, C para casado): ")
ubicacion = input("¿vive en una ciudad (U) o en el campo (R)? ")

if verificar_aprobacion(ingreso, año_nacimiento, num_hijos, años_pertenencia, estado_civil, ubicacion):
    print(obtener_respuesta_aleatoria(respuestas_aprobado))
else:
    print(obtener_respuesta_aleatoria(respuestas_rechazado))
