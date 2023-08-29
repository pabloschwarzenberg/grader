#Aprobación de créditos
#Solicitar datos al cliente
ingreso = float(input("Ingrese su ingreso en pesos: "))
ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anos_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S=soltero, C=casado): ")
ubicacion = input("Ingrese su ubicación (U=urbano, R=rural): ")

#Datos y aprobación o rechazo

aprobado = False

if anos_pertenencia > 10 and num_hijos >= 2:
    aprobado = True
elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - ano_nacimiento) <= 55:
    aprobado = True
elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
    aprobado = True
elif ingreso > 3500000 and anos_pertenencia > 5:
    aprobado = True
elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
    aprobado = True

#Imprimir el resultado
if aprobado:
    print("APROBADO")
else:
    print("RECHAZADO")