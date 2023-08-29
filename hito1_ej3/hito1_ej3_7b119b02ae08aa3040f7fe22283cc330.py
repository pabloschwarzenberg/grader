#Aprobación de créditos
# Preguntar al cliente sus datos
ingreso = float(input("Ingrese su ingreso en pesos: "))
ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese su número de hijos: "))
anos_membresia = int(input("Ingrese su número de años en la membresía del banco: "))
estado_civil = input("Ingrese su estado civil (S/C): ")
vive_en_campo = input("¿Vive en campo o en ciudad? (U/R): ")

# Procesar los datos del cliente
if anos_membresia > 10 and num_hijos >= 2:
    print("APROBADO")
elif estado_civil == "C" and num_hijos > 3 and ano_nacimiento >= 45 and ano_nacimiento <= 55:
    print("APROBADO")
elif ingreso > 2500000 and estado_civil == "S" and vive_en_campo == "U":
    print("APROBADO")
elif ingreso > 3500000 and anos_membresia > 5 and num_hijos < 2:
    print("APROBADO")
elif vive_en_campo == "R" and estado_civil == "C" and num_hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")      