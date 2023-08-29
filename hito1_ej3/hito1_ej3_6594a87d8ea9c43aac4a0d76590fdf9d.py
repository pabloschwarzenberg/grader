#Aprobación de créditos
def aprobar_credito(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion):
    if anos_pertenencia > 10 and num_hijos >= 2:
        return "APROBADO"
    elif estado_civil == "C" and num_hijos > 3 and ano_nacimiento >= 45 and ano_nacimiento <= 55:
        return "APROBADO"
    elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return "APROBADO"
    elif ingreso > 3500000 and anos_pertenencia > 5:
        return "APROBADO"
    elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return "APROBADO"
    else:
        return "RECHAZADO"

ingreso = float(input("Ingrese el ingreso del cliente (en pesos): "))
ano_nacimiento = int(input("Ingrese el año de nacimiento del cliente: "))
num_hijos = int(input("Ingrese el número de hijos del cliente: "))
anos_pertenencia = int(input("Ingrese los años de pertenencia al banco del cliente: "))
estado_civil = input("Ingrese el estado civil del cliente ('S' para soltero, 'C' para casado): ")
ubicacion = input("Ingrese la ubicación del cliente ('U' para urbano, 'R' para rural): ")

resultado = aprobar_credito(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion)
print("Resultado:", resultado)
    