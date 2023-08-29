#Aprobación de créditos
def aprobar_credito(ingreso, año_nacimiento, num_hijos, años_pertenencia, estado_civil, ubicacion):
    if años_pertenencia > 10 and num_hijos >= 2:
        return True
    elif estado_civil == "C" and num_hijos > 3 and año_nacimiento >= 45 and año_nacimiento <= 55:
        return True
    elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return True
    elif ingreso > 3500000 and años_pertenencia > 5:
        return True
    elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return True
    else:
        return False

# Solicitar al cliente que ingrese sus datos
ingreso = float(input("Ingrese su ingreso mensual (en pesos): "))
año_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
años_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S: soltero, C: casado): ")
ubicacion = input("Ingrese su ubicación (U: urbano, R: rural): ")

# Determinar si se aprueba o se rechaza el crédito
if aprobar_credito(ingreso, año_nacimiento, num_hijos, años_pertenencia, estado_civil, ubicacion):
    print("APROBADO")
else:
    print("RECHAZADO")
     