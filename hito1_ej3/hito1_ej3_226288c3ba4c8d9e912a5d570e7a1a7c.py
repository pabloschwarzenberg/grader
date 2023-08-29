def decidir_aprobacion(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion):
    if anos_pertenencia > 10 and num_hijos >= 2:
        return "APROBADO"  # Se aprueba si el cliente pertenece más de 10 años al banco y tiene dos o más hijos
    elif estado_civil == "C" and num_hijos > 3 and ano_nacimiento >= 45 and ano_nacimiento <= 55:
        return "APROBADO"  # Se aprueba si el cliente es casado, tiene más de tres hijos y tiene entre 45 y 55 años
    elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return "APROBADO"  # Se aprueba si el cliente tiene ingresos superiores a $2.500.000, es soltero y vive en la ciudad
    elif ingreso > 3500000 and anos_pertenencia > 5:
        return "APROBADO"  # Se aprueba si el cliente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
    elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return "APROBADO"  # Se aprueba si el cliente vive en el campo, es casado y tiene menos de dos hijos
    else:
        return "RECHAZADO"  # Se rechaza en los demás casos

# Pedimos al cliente que ingrese su información personal
ingreso = float(input("Ingrese su ingreso en pesos: "))
ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anos_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese su ubicación (U para urbano, R para rural): ")

# Verificamos si se aprueba o se rechaza el crédito
decision = decidir_aprobacion(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion)

# Imprimimos el resultado
print(decision)