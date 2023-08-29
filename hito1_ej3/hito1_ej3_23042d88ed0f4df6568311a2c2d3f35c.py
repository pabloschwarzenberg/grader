def aprobar_credito(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion):
    if anos_pertenencia > 10 and num_hijos >= 2:
        return "APROBADO"  # Pertenece más de 10 años al banco y tiene dos o más hijos
    elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - ano_nacimiento) <= 55:
        return "APROBADO"  # Es casado, tiene más de tres hijos y tiene entre 45 y 55 años
    elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return "APROBADO"  # Tiene ingresos superiores a $2.500.000, es soltero y vive en la ciudad
    elif ingreso > 3500000 and anos_pertenencia > 5:
        return "APROBADO"  # Tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
    elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return "APROBADO"  # Vive en el campo, es casado y tiene menos de dos hijos
    else:
        return "RECHAZADO"  # No cumple ninguna de las reglas para la aprobación del crédito

# Solicitar entrada al cliente
ingreso = int(input("Ingrese su ingreso mensual en pesos: "))
ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anos_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese su ubicación (U para urbano, R para rural): ")

# Llamar a la función y mostrar el resultado
resultado = aprobar_credito(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion)
print(resultado)
