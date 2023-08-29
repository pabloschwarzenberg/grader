# Solicitar los datos al cliente
ingreso = int(input("Ingrese su ingreso en pesos: "))
ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anos_banco = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese su ubicación (U para urbano, R para rural): ")

# Determinar si se aprueba el crédito
aprobado = False

if anos_banco > 10 and num_hijos >= 2:
    # Regla 1: Más de 10 años en el banco y 2 o más hijos
    aprobado = True
elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - ano_nacimiento) <= 55:
    # Regla 2: Casado, más de 3 hijos y edad entre 45 y 55 años
    aprobado = True
elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
    # Regla 3: Ingresos superiores a $2.500.000, soltero y vive en la ciudad
    aprobado = True
elif ingreso > 3500000 and anos_banco > 5:
    # Regla 4: Ingresos superiores a $3.500.000 y más de 5 años en el banco
    aprobado = True
elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
    # Regla 5: Vive en el campo, casado y menos de 2 hijos
    aprobado = True

# Imprimir el resultado
if aprobado:
    print("APROBADO")
else:
    print("RECHAZADO")
      