#Aprobación de créditos
# Solicitamos la información del cliente
ingreso = int(input("Ingrese su ingreso en pesos: "))
anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese su número de hijos: "))
anos_pertenencia = int(input("Ingrese sus años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S: soltero, C: casado): ")
lugar_vivienda = input("Ingrese su lugar de vivienda (U: urbano, R: rural): ")

# Calculamos la edad del cliente
edad = 2023 - anio_nacimiento  # Asumiendo que el año actual es 2023

# Aplicamos las reglas del banco
if (anos_pertenencia > 10 and num_hijos >= 2):
    print("APROBADO")
elif (estado_civil == "C" and num_hijos > 3 and 45 <= edad <= 55):
    print("APROBADO")
elif (ingreso > 2500000 and estado_civil == "S" and lugar_vivienda == "U"):
    print("APROBADO")
elif (ingreso > 3500000 and anos_pertenencia > 5):
    print("APROBADO")
elif (lugar_vivienda == "R" and estado_civil == "C" and num_hijos < 2):
    print("APROBADO")
else:
    print("RECHAZADO")