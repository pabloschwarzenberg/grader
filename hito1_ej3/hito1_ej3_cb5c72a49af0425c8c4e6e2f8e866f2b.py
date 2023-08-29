#Aprobación de créditos
    #Aprobación de credito
from _ast import If

ingreso_pesos = int(input("ingreso sueldo: $"))
nacimiento = int(input("ingreso nacimiento: "))
hijos = int(input("cantidad de hijos: "))
permanencia_banco = int(input("tiempo en el banco: "))
estado_civil = int(input("estado civil, 'S' - Soltero, 'C' - casado: "))
vivienda = input(("vive en: 'U' - urbano, 'R' - rural: ")))
edad = (2021 - nacimiento)

if permanencia_banco > 10 and hijos >=2:
    print("APROBADO")

If estado_civil == 'C' and hijos >=3 and edad >= 45 and edad <=55
    print("APROBADO")

if ingreso_pesos > 2500000 and estado_civil >= 'S' and vivienda == 'U':
    print("APROBADO")

if ingreso_pesos > 3500000 and permanencia_banco >= 5:
    print("APROBADO")

if vivienda == 'R' and estado_civil == 'C' and  hijos < 2:
    print("APROBADO")

print("RECHAZADO")