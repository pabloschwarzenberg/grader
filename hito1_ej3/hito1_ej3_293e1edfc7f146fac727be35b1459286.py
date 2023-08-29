#Aprobación de créditos
año = 2020
ingresos = float(input("Ingresos: "))
nacimiento = int(input("Nacimiento: "))
edad = año - nacimiento
hijos = int(input("Hijo/s: "))
antigüedad = int(input("Antigüedad: "))
estado_civil = input("Soltero (S) / Casado (C): ")
estado_civil = estado_civil.upper()
localidad = input("Urbano (U) / Rural (R): ")
localidad = localidad.upper()
petición = "RECHAZADO"

if antigüedad > 10 and hijos >= 2:
    petición = "APROBADO"
elif estado_civil == "C" and hijos > 3 and (45 <= edad <= 55):
    petición = "APROBADO"
elif ingresos > 2500000 and estado_civil == "S" and localidad == "U":
    petición = "APROBADO"
elif ingresos > 3500000 and antigüedad > 5:
    petición = "APROBADO"
elif localidad == "R" and estado_civil == "C" and hijos < 2:
    petición = "APROBADO"

print(petición)