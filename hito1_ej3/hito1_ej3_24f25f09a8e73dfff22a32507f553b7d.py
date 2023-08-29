#Aprobación de créditos
def aprobar_credito(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion):
    if anos_pertenencia > 10 and num_hijos >= 2:
        return "APROBADO"
    
    if estado_civil == "C" and num_hijos > 3 and ano_nacimiento >= 45 and ano_nacimiento <= 55:
        return "APROBADO"
    
    if ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return "APROBADO"
    
    if ingreso > 3500000 and anos_pertenencia > 5:
        return "APROBADO"
    
    if ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return "APROBADO"
    
    return "RECHAZADO"

# Solicitar al usuario ingresar los datos personales
ingreso = int(input("Ingrese su ingreso (en pesos): "))
ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anos_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese su ubicación (U para urbano, R para rural): ")

# Verificar la aprobación del crédito
resultado = aprobar_credito(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion)

# Mostrar el resultado
print("Resultado:", resultado)