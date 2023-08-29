#Aprobación de créditos
def aprobar_credito(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion):
    if anos_pertenencia > 10 and num_hijos >= 2:
        return "APROBADO"
    
    if estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - ano_nacimiento) <= 55:
        return "APROBADO"
    
    if ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return "APROBADO"
    
    if ingreso > 3500000 and anos_pertenencia > 5:
        return "APROBADO"
    
    if ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return "APROBADO"
    
    return "RECHAZADO"

# Solicitar los datos al cliente
ingreso = int(input("Ingrese el ingreso mensual en pesos: "))
ano_nacimiento = int(input("Ingrese el año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anos_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese el estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese la ubicación (U para urbano, R para rural): ")

# Verificar si se aprueba o rechaza el crédito
decision = aprobar_credito(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion)

# Imprimir el resultado
print(decision)
      