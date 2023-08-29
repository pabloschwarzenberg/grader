#Aprobación de créditos
def verificar_aprobacion_credito(ingreso, anio_nacimiento, num_hijos, anios_pertenencia, estado_civil, lugar_residencia):
    if anios_pertenencia > 10 and num_hijos >= 2:
        return True

    if estado_civil == "C" and num_hijos > 3 and anio_nacimiento >= 45 and anio_nacimiento <= 55:
        return True

    if ingreso > 2500000 and estado_civil == "S" and lugar_residencia == "U":
        return True

    if ingreso > 3500000 and anios_pertenencia > 5:
        return True

    if lugar_residencia == "R" and estado_civil == "C" and num_hijos < 2:
        return True  

    return False
    
    # Pedir al cliente que ingrese su información personal
ingreso = int(input("Ingrese su ingreso en pesos: "))
anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anios_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
lugar_residencia = input("Ingrese si vive en campo (R para rural) o ciudad (U para urbano): ")

# Verificar la aprobación del crédito
aprobado = verificar_aprobacion_credito(ingreso, anio_nacimiento, num_hijos, anios_pertenencia, estado_civil, lugar_residencia)

# Imprimir el resultado
if aprobado:
    print("APROBADO")
else:
    print("RECHAZADO")