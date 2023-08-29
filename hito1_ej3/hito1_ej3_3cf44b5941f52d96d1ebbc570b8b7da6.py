#Aprobación de créditos
ingreso = float(input("Ingrese su ingreso en pesos: "))
an = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
ap = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese su ubicación (U para urbano, R para rural): ")

aprobado = False  # Variable para verificar si el crédito está aprobado

if ap > 10 and num_hijos >= 2:
    aprobado = True

if estado_civil == "C" and num_hijos > 3 and an >= 45 and an <= 55:
    aprobado = True

if ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
    aprobado = True

if ingreso > 3500000 and ap > 5:
    aprobado = True

if ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
    aprobado = True

if aprobado:
    print("APROBADO")
else:
    print("RECHAZADO")