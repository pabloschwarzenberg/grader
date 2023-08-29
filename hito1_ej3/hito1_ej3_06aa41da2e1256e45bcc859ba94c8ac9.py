#Aprobación de créditos
def verificar_aprobacion(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, lugar_residencia):
    if anos_pertenencia > 10 and num_hijos >= 2:
        return "APROBADO"
    elif estado_civil == "C" and num_hijos > 3 and ano_nacimiento >= 45 and ano_nacimiento <= 55:
        return "APROBADO"
    elif ingreso > 2500000 and estado_civil == "S" and lugar_residencia == "U":
        return "APROBADO"
    elif ingreso > 3500000 and anos_pertenencia > 5:
        return "APROBADO"
    elif lugar_residencia == "R" and estado_civil == "C" and num_hijos < 2:
        return "APROBADO"
    else:
        return "RECHAZADO"

# Solicitar al usuario que ingrese los datos
ingreso = int(input("Ingrese su ingreso en pesos: "))
ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anos_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
lugar_residencia = input("Ingrese si vive en campo (R para rural) o ciudad (U para urbano): ")

# Verificar la aprobación del crédito
resultado = verificar_aprobacion(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, lugar_residencia)

# Imprimir el resultado
print("Resultado:", resultado)
