def aprobar_credito(ingreso, anio_nacimiento, num_hijos, anios_pertenencia, estado_civil, ubicacion):
    if anios_pertenencia > 10 and num_hijos >= 2:
        return True
    elif estado_civil == "C" and num_hijos > 3 and anio_nacimiento >= 45 and anio_nacimiento <= 55:
        return True
    elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return True
    elif ingreso > 3500000 and anios_pertenencia > 5:
        return True
    elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return True
    else:
        return False

ingreso = float(input("Ingrese su ingreso (en pesos): "))
anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anhos_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese su ubicación (U para urbano, R para rural): ")

if aprobar_credito(ingreso, anio_nacimiento, num_hijos, anhos_pertenencia, estado_civil, ubicacion):
    print("APROBADO")
else:
    print("RECHAZADO")