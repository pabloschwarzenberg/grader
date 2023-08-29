#Aprobación de créditos
def solicitar_datos():
    ingreso = int(input("Ingrese su ingreso mensual en pesos: "))
    año_nacimiento = int(input("Ingrese su año de nacimiento: "))
    num_hijos = int(input("Ingrese el número de hijos que tiene: "))
    años_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
    estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
    ubicacion = input("Ingrese su ubicación (U para urbano, R para rural): ")
    return ingreso, año_nacimiento, num_hijos, años_pertenencia, estado_civil, ubicacion

def evaluar_credito(ingreso, año_nacimiento, num_hijos, años_pertenencia, estado_civil, ubicacion):
    if años_pertenencia > 10 and num_hijos >= 2:
        return True
    elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - año_nacimiento) <= 55:
        return True
    elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return True
    elif ingreso > 3500000 and años_pertenencia > 5:
        return True
    elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return True
    else:
        return False

ingreso, año_nacimiento, num_hijos, años_pertenencia, estado_civil, ubicacion = solicitar_datos()
aprobado = evaluar_credito(ingreso, año_nacimiento, num_hijos, años_pertenencia, estado_civil, ubicacion)

if aprobado:
    print("APROBADO")
else:
    print("RECHAZADO")
      