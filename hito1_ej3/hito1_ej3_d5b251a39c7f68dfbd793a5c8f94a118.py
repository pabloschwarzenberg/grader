#Aprobación de créditos
def aprobar_credito(ingreso, nacimiento, hijos, anos_banco, estado_civil, ubicacion):
    if anos_banco > 10 and hijos >= 2:
        return "APROBADO"
    elif estado_civil == "C" and hijos > 3 and nacimiento >= 45 and nacimiento <= 55:
        return "APROBADO"
    elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return "APROBADO"
    elif ingreso > 3500000 and anos_banco > 5:
        return "APROBADO"
    elif ubicacion == "R" and estado_civil == "C" and hijos < 2:
        return "APROBADO"
    else:
        return "RECHAZADO"

# Solicitar al cliente que ingrese sus datos
ingreso = int(input("Ingrese su ingreso en pesos: "))
nacimiento = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese el número de hijos: "))
anos_banco = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese su ubicación (U para urbano, R para rural): ")

# Determinar si el crédito es aprobado o rechazado y mostrar el resultado
resultado = aprobar_credito(ingreso, nacimiento, hijos, anos_banco, estado_civil, ubicacion)
print("Resultado:", resultado)