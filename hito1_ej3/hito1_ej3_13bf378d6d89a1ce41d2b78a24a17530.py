#Aprobación de créditos
def aprobar_credito(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion):
    # Verificar si el cliente pertenece más de 10 años al banco y tiene dos o más hijos
    if anos_pertenencia > 10 and num_hijos >= 2:
        return "APROBADO"
    
    # Verificar si el cliente es casado, tiene más de tres hijos y tiene entre 45 y 55 años
    if estado_civil == "C" and num_hijos > 3 and ano_nacimiento >= (2023 - 55) and ano_nacimiento <= (2023 - 45):
        return "APROBADO"
    
    # Verificar si el cliente tiene ingresos superiores a $2.500.000, es soltero y vive en la ciudad
    if ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return "APROBADO"
    
    # Verificar si el cliente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
    if ingreso > 3500000 and anos_pertenencia > 5:
        return "APROBADO"
    
    # Verificar si el cliente vive en el campo, es casado y tiene menos de dos hijos
    if ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return "APROBADO"
    
    # Si ninguna de las condiciones anteriores se cumple, se rechaza el crédito
    return "RECHAZADO"


# Solicitar los datos al cliente
ingreso = int(input("Ingrese su ingreso en pesos: "))
ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anos_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese su ubicación (U para urbano, R para rural): ")

# Obtener el resultado
resultado = aprobar_credito(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion)

# Imprimir el resultado
print("El crédito es:", resultado)
   