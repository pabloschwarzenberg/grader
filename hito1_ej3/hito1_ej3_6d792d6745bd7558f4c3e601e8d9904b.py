#Aprobación de créditos
 # Pedir al usuario que ingrese la información personal
ingreso = float(input("Ingrese su ingreso en pesos: "))
anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
numero_hijos = int(input("Ingrese el número de hijos: "))
anios_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
lugar_residencia = input("Ingrese su lugar de residencia (U para urbano, R para rural): ")


aprobado = False

if anios_pertenencia > 10 and numero_hijos >= 2:
    aprobado = True
elif estado_civil == "C" and numero_hijos > 3 and 45 <= (2023 - anio_nacimiento) <= 55:
    aprobado = True
elif ingreso > 2500000 and estado_civil == "S" and lugar_residencia == "U":
    aprobado = True
elif ingreso > 3500000 and anios_pertenencia > 5:
    aprobado = True
elif lugar_residencia == "R" and estado_civil == "C" and numero_hijos < 2:
    aprobado = True


if aprobado:
    print("APROBADO")
else:
    print("RECHAZADO")
     