#Aprobación de créditos
def aprobar_credito(ingreso, año_nacimiento, num_hijos, años_banco, estado_civil, ubicacion):
    if años_banco > 10 and num_hijos >= 2:
        return "APROBADO"
    elif estado_civil == "C" and num_hijos > 3 and año_nacimiento >= 45 and año_nacimiento <= 55:
        return "APROBADO"
    elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return "APROBADO"
    elif ingreso > 3500000 and años_banco > 5:
        return "APROBADO"
    elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return "APROBADO"
    else:
        return "RECHAZADO"

# Solicitar los datos al cliente
ingreso = float(input("Ingrese el ingreso en pesos: "))
año_nacimiento = int(input("Ingrese el año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
años_banco = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese el estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese la ubicación (U para urbano, R para rural): ")

# Determinar la aprobación del crédito
resultado = aprobar_credito(ingreso, año_nacimiento, num_hijos, años_banco, estado_civil, ubicacion)

# Imprimir el resultado
print("El crédito está", resultado)
      