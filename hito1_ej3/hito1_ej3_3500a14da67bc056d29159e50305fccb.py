#Aprobación de créditos
ingreso = float(input("Ingrese su ingreso en pesos: "))
nacimiento = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese el número de hijos: "))
anos = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese su ubicación (U para urbano, R para rural): ")

aprobado = False

if anos > 10 and hijos >= 2:
    aprobado = True
elif estado_civil == "C" and hijos > 3 and 45 <= (2023 - nacimiento) <= 55:
    aprobado = True
elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
    aprobado = True
elif ingreso > 3500000 and anos > 5:
    aprobado = True
elif ubicacion == "R" and estado_civil == "C" and hijos < 2:
    aprobado = True

if aprobado:
    print("APROBADO")
else:
    print("RECHAZADO")