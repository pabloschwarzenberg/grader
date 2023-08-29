#Aprobación de créditos
def verificar_aprobacion_credito(ingreso, año_nacimiento, num_hijos, años_pertenencia, estado_civil, lugar_residencia):
    if años_pertenencia > 10 and num_hijos >= 2:
        return True
    elif estado_civil == "C" and num_hijos > 3 and año_nacimiento >= 45 and año_nacimiento <= 55:
        return True
    elif ingreso > 2500000 and estado_civil == "S" and lugar_residencia == "U":
        return True
    elif ingreso > 3500000 and años_pertenencia > 5:
        return True
    elif lugar_residencia == "R" and estado_civil == "C" and num_hijos < 2:
        return True
    else:
        return False

ingreso = int(input("Ingrese su ingreso en pesos: "))
año_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
años_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
lugar_residencia = input("Ingrese su lugar de residencia (U para urbano, R para rural): ")

if verificar_aprobacion_credito(ingreso, año_nacimiento, num_hijos, años_pertenencia, estado_civil, lugar_residencia):
    print("APROBADO")
else:
    print("RECHAZADO")