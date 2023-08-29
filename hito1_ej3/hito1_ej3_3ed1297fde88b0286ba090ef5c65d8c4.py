ingreso = float(input())
anio_nacimiento = int(input())
num_hijos = int(input())
anios_pertenencia = int(input())
estado_civil = input()
tipo_vivienda = input()

aprobado = False

if anios_pertenencia > 10 and num_hijos >= 2:
    aprobado = True
elif estado_civil == "C" and num_hijos > 3 and anio_nacimiento >= 45 and anio_nacimiento <= 55:
    aprobado = True
elif ingreso > 2500000 and estado_civil == "S" and tipo_vivienda == "U":
    aprobado = True
elif ingreso > 3500000 and anios_pertenencia > 5:
    aprobado = True
elif tipo_vivienda == "R" and estado_civil == "C" and num_hijos < 2:
    aprobado = True

if aprobado:
    print("APROBADO")
else:
    print("RECHAZADO")

      