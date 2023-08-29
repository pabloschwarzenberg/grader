#Aprobación de créditos
# Solicitamos al usuario sus datos
ingreso = int(input("Ingrese su ingreso en pesos: "))
anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese su número de hijos: "))
anos_pertenencia = int(input("Ingrese sus años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S: soltero, C: casado): ")
vive = input("Indique si vive en el campo o ciudad (U: urbano, R: rural): ")

# Calculamos la edad del cliente
edad = 2023 - anio_nacimiento

# Aplicamos las reglas del banco para decidir si se aprueba o no el crédito
if anos_pertenencia > 10 and num_hijos >= 2:
    print("APROBADO")
elif estado_civil == "C" and num_hijos > 3 and 45 <= edad <= 55:
    print("APROBADO")
elif ingreso > 2500000 and estado_civil == "S" and vive == "U":
    print("APROBADO")
elif ingreso > 3500000 and anos_pertenencia > 5:
    print("APROBADO")
elif vive == "R" and estado_civil == "C" and num_hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
     

      