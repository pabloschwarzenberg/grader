#Aprobación de créditos
def verificar_aprobacion(ingreso, anio_nacimiento, num_hijos, anios_banco, estado_civil, lugar_residencia):
    if anios_banco > 10 and num_hijos >= 2:
        return True
    elif estado_civil == "C" and num_hijos > 3 and anio_nacimiento >= 45 and anio_nacimiento <= 55:
        return True
    elif ingreso > 2500000 and estado_civil == "S" and lugar_residencia == "U":
        return True
    elif ingreso > 3500000 and anios_banco > 5:
        return True
    elif lugar_residencia == "R" and estado_civil == "C" and num_hijos < 2:
        return True
    else:
        return False

ingreso = float(input("Ingrese el ingreso mensual en pesos: "))
anio_nacimiento = int(input("Ingrese el año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anios_banco = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese el estado civil (S para soltero, C para casado): ")
lugar_residencia = input("Ingrese el lugar de residencia (U para urbano, R para rural): ")

if verificar_aprobacion(ingreso, anio_nacimiento, num_hijos, anios_banco, estado_civil, lugar_residencia):
    print("APROBADO")
else:
    print("RECHAZADO")
      