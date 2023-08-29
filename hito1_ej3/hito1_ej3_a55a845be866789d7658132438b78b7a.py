#Aprobación de créditos
def solicitar_datos_cliente():
    ingreso = float(input("Ingrese su ingreso en pesos: "))
    ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
    num_hijos = int(input("Ingrese el número de hijos: "))
    anos_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
    estado_civil = input("Ingrese su estado civil (S - soltero, C - casado): ")
    ubicacion = input("Ingrese su ubicación (U - urbano, R - rural): ")
    
    return ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion

def aprobar_credito(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion):
    if anos_pertenencia > 10 and num_hijos >= 2:
        return True
    elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - ano_nacimiento) <= 55:
        return True
    elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return True
    elif ingreso > 3500000 and anos_pertenencia > 5:
        return True
    elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return True
    else:
        return False

# Solicitar los datos al cliente
ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion = solicitar_datos_cliente()

# Verificar si se aprueba o se rechaza el crédito
if aprobar_credito(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion):
    print("APROBADO")
else:
    print("RECHAZADO")
     