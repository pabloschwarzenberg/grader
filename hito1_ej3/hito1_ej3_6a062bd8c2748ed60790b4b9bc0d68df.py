#Aprobación de créditos
def aprobar_credito(ingreso, anio_nacimiento, num_hijos, anios_banco, estado_civil, ubicacion):
    if anios_banco > 10 and num_hijos >= 2:
        return "APROBADO"
    elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - anio_nacimiento) <= 55:
        return "APROBADO"
    elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return "APROBADO"
    elif ingreso > 3500000 and anios_banco > 5:
        return "APROBADO"
    elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return "APROBADO"
    else:
        return "RECHAZADO"

ingreso = int(input("Ingrese el ingreso mensual en pesos: "))
anio_nacimiento = int(input("Ingrese el año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anios_banco = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese el estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese la ubicación (U para urbano, R para rural): ")

resultado = aprobar_credito(ingreso, anio_nacimiento, num_hijos, anios_banco, estado_civil, ubicacion)
print("Estado del crédito:", resultado)
      