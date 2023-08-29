#Aprobación de créditos
ingreso = int(input("Ingreso (en pesos): "))
nacimiento = int(input("Año de nacimiento: "))
hijos = int(input("Número de hijos: "))
años = int(input("Años de pertenencia al banco: "))
civil = input('Estado civil ("S": soltero, "C", casado): ')
vive = input('Si vive en campo o ciudad ("U": urbano, "R": rural): ')

if años >= 10 and hijos >= 2:
    print("APROBADO")
if civil == "C" and hijos >= 3 and 45 <= (2020-nacimiento) <= 55:
    print("APROBADO")
if ingreso >= 2500000 and civil == "S" and vive == "U":
    print("APROBADO")
if ingreso >= 3500000 and años >= 5:
    print("APROBADO")
if vive == "R" and civil == "C" and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
