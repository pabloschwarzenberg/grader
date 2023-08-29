def verificar_aprobacion(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, lugar_residencia):
    if anos_pertenencia > 10 and num_hijos >= 2:
        return True

    if estado_civil == "C" and num_hijos > 3 and ano_nacimiento >= 45 and ano_nacimiento <= 55:
        return True

    if ingreso > 2500000 and estado_civil == "S" and lugar_residencia == "U":
        return True

    if ingreso > 3500000 and anos_pertenencia > 5:
        return True

    if lugar_residencia == "R" and estado_civil == "C" and num_hijos < 2:
        return True

    return False

ingreso = float(input("Ingrese su ingreso (en pesos): "))
ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anos_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
lugar_residencia = input("Ingrese su lugar de residencia (U para urbano, R para rural): ")

if verificar_aprobacion(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, lugar_residencia):
    print("APROBADO")
else:
    print("RECHAZADO")
      