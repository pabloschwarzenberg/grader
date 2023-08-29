#Aprobación de créditos

ingresos = int(input(("ingrese sueldo: $")))
nacimiento = int(input(("ingrese año de nacimiento:")))
hijos = int(input(("ingrese numero de hijos:")))
anios = int(input(("ingrese los anios que lleva en el banco:")))
est_civil = str(input(("ingrese estado civil 'S' si es soltero y 'C' si es casado:")))
lugar = str(input(("ingrese sector donde vive, si es rural 'R' y si es urbano 'U':")))
edad = (2021-nacimiento)

if anios > 10 and hijos >= 2:
    print("APROBADO")
if est_civil == 'C' and hijos > 3 and edad >= 45 and edad <= 55:
    print("APROBADO")
if ingresos > 2500000 and est_civil >= 'S' and lugar == 'U':
    print("APROBADO")
if ingresos > 3500000 and anios >= 5:
    print("APROBADO")
if lugar == 'R' and est_civil == 'C' and hijos < 2:
    print("APROBADO")
print("Rechazado")

