def aprobar_credito(ingreso, ano_nacimiento, num_hijos, anos_banco, estado_civil, ubicacion):
    if anos_banco > 10 and num_hijos >= 2:
        return True
    elif estado_civil == "C" and num_hijos > 3 and ano_nacimiento >= 45 and año_nacimiento <= 55:
        return True
    elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return True
    elif ingreso > 3500000 and anos_banco > 5:
        return True
    elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return True
    else:
        return False

# Solicitar al usuario ingresar los datos personales
ingreso = float(input("Ingrese su ingreso en pesos: "))
ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anos_banco = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese su ubicación (U para urbano, R para rural): ")

# Verificar si se aprueba o se rechaza el crédito
if aprobar_credito(ingreso, ano_nacimiento, num_hijos, anos_banco, estado_civil, ubicacion):
    print("APROBADO")
else:
    print("RECHAZADO")
    