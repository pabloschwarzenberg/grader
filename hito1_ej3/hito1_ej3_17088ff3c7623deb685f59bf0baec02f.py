#Aprobación de créditos
ingreso = float(input("Ingrese el ingreso mensual en pesos: "))
anio_nacimiento = int(input("Ingrese el año de nacimiento: "))
numero_hijos = int(input("Ingrese el número de hijos: "))
anios_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese el estado civil (S para soltero, C para casado): ")
tipo_vivienda = input("Ingrese el tipo de vivienda (U para urbano, R para rural): ")

aprobado = False

if anios_pertenencia > 10 and numero_hijos >= 2:
    aprobado = True
elif estado_civil == 'C' and numero_hijos > 3 and 45 <= (2023 - anio_nacimiento) <= 55:
    aprobado = True
elif ingreso > 2500000 and estado_civil == 'S' and tipo_vivienda == 'U':
    aprobado = True
elif ingreso > 3500000 and anios_pertenencia > 5:
    aprobado = True
elif tipo_vivienda == 'R' and estado_civil == 'C' and numero_hijos < 2:
    aprobado = True

if aprobado:
    print("APROBADO")
else:
    print("RECHAZADO")
