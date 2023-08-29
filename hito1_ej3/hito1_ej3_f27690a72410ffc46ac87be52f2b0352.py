#Aprobación de créditos
def verificar_aprobacion(ingreso, nacimiento, hijos, años_banco, estado_civil, ubicacion):
    if años_banco > 10 and hijos >= 2:
        return True
    elif estado_civil == "C" and hijos > 3 and nacimiento >= 45 and nacimiento <= 55:
        return True
    elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return True
    elif ingreso > 3500000 and años_banco > 5:
        return True
    elif ubicacion == "R" and estado_civil == "C" and hijos < 2:
        return True
    else:
        return False

ingreso = int(input("Ingrese el ingreso mensual en pesos: "))
nacimiento = int(input("Ingrese el año de nacimiento: "))
hijos = int(input("Ingrese el número de hijos: "))
años_banco = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese el estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese la ubicación (U para urbano, R para rural): ")

aprobado = verificar_aprobacion(ingreso, nacimiento, hijos, años_banco, estado_civil, ubicacion)

if aprobado:
    print("APROBADO")
else:
    print("RECHAZADO")

      