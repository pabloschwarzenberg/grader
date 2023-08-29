#Aprobación de créditos
def aprobar_credito(ingreso, ano_nacimiento, num_hijos, anos_banco, estado_civil, ubicacion):
    edad = 2023 - ano_nacimiento

    if anos_banco > 10 and num_hijos >= 2:
        return "APROBADO"
    elif estado_civil == "C" and num_hijos > 3 and edad >= 45 and edad <= 55:
        return "APROBADO"
    elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return "APROBADO"
    elif ingreso > 3500000 and anos_banco > 5:
        return "APROBADO"
    elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return "APROBADO"
    else:
        return "RECHAZADO"

# Pedir al cliente que ingrese los datos
ingreso = int(input("Ingrese el ingreso mensual (en pesos): "))
ano_nacimiento = int(input("Ingrese el año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anos_banco = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese el estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese la ubicación (U para urbano, R para rural): ")

# Llamar a la función para determinar si se aprueba o se rechaza el crédito
resultado = aprobar_credito(ingreso, ano_nacimiento, num_hijos, anos_banco, estado_civil, ubicacion)

# Imprimir el resultado
print("El crédito es:", resultado)
