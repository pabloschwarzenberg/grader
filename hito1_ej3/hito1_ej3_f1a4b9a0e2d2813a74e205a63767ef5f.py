#Aprobación de créditos
def aprobar_credito(ingreso, nacimiento, hijos, años_banco, estado_civil, ubicacion):
    if años_banco > 10 and hijos >= 2:
        return True  

    if estado_civil == "C" and hijos > 3 and nacimiento >= 1973 and nacimiento <= 1983:
        return True 

    if ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return True  

    if ingreso > 3500000 and años_banco > 5:
        return True  

    if ubicacion == "R" and estado_civil == "C" and hijos < 2:
        return True  

    return False  

ingreso = int(input("Ingrese el ingreso en pesos: "))
nacimiento = int(input("Ingrese el año de nacimiento: "))
hijos = int(input("Ingrese el número de hijos: "))
años_banco = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese el estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese la ubicación (U para urbano, R para rural): ")

if aprobar_credito(ingreso, nacimiento, hijos, años_banco, estado_civil, ubicacion):
    print("APROBADO")
else:
    print("RECHAZADO")
