#Aprobación de créditos
def aprobar_credito(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion):
    # Regla 1: Cliente pertenece más de 10 años al banco y tiene dos o más hijos
    if anos_pertenencia > 10 and num_hijos >= 2:
        return "APROBADO"    
    # Regla 2: Cliente es casado, tiene más de tres hijos y tiene entre 45 y 55 años
    if estado_civil == "C" and num_hijos > 3 and 45 <= ano_nacimiento <= 55:
        return "APROBADO"    
    # Regla 3: Cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad
    if ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return "APROBADO"    
    # Regla 4: Cliente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
    if ingreso > 3500000 and anos_pertenencia > 5:
        return "APROBADO"    
    # Regla 5: Cliente vive en el campo, es casado y tiene menos de dos hijos
    if ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return "APROBADO"    
    # Si ninguna regla se cumple, el crédito es rechazado
    return "RECHAZADO"
# Solicitar datos al cliente
ingreso = float(input("Ingrese su ingreso mensual en pesos: "))
ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anos_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S: soltero, C: casado): ")
ubicacion = input("Ingrese su ubicación (U: urbano, R: rural): ")
# Llamar a la función para determinar si se aprueba o rechaza el crédito
resultado = aprobar_credito(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion)
# Imprimir el resultado
print("Resultado:", resultado)  