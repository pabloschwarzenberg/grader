#Aprobación de créditos
# Pedimos los datos al cliente
ingreso = int(input("Ingrese su ingreso en pesos: "))
ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese su número de hijos: "))
anos_pertenencia = int(input("Ingrese sus años de pertenencia al banco: "))
estado_civil = input("Ingrese si es soltero (S) o casado (C): ")
ubicacion = input("Ingrese si vive en la ciudad (U) o en el campo (R): ")

# Verificamos si cumple alguna de las condiciones para aprobar el crédito
if anos_pertenencia > 10 and num_hijos >= 2:
    print("APROBADO")
elif estado_civil == "C" and num_hijos > 3 and 45 <=(2023 - ano_nacimiento) <= 55:
    print("APROBADO")
elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
    print("APROBADO")
elif ingreso > 3500000 and anos_pertenencia > 5:
    print("APROBADO")
elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
     