#Aprobación de créditos
# Solicitar al cliente su información
ingreso = float(input("Ingrese su ingreso en pesos: "))
ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anos_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese su ubicación (U para urbano, R para rural): ")

# Verificar las reglas para decidir si se aprueba el crédito
if anos_pertenencia > 10 and num_hijos >= 2:
    # Regla 1: Pertenece más de 10 años al banco y tiene dos o más hijos
    print("APROBADO")
elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - ano_nacimiento) <= 55:
    # Regla 2: Es casado, tiene más de tres hijos y tiene entre 45 y 55 años
    print("APROBADO")
elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
    # Regla 3: Ingresos superiores a $2.500.000, es soltero y vive en la ciudad
    print("APROBADO")
elif ingreso > 3500000 and anos_pertenencia > 5:
    # Regla 4: Ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
    print("APROBADO")
elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
    # Regla 5: Vive en el campo, es casado y tiene menos de dos hijos
    print("APROBADO")
else:
    # No se cumple ninguna de las reglas anteriores
    print("RECHAZADO")
