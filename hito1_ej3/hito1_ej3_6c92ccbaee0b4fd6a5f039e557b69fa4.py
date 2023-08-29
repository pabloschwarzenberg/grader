#Aprobación de créditos
#Aprobación de créditos
Ingresos = int(input("Cuales son sus ingresos: $"))
Anno = int(input("Cual es su año de nacimiento: "))
Edad = int(2021-Anno)
Hijos = int(input("Cuantos hijos tiene: "))
AnnosBanco = int(input("Cuantos años lleva en este banco: "))
EstadoCivivl = input("¿esta soltero 'S' o casado 'C'?:")
Vivienda = input("¿Vive en un lugar rural 'R' o urbano 'U'?")
if (AnnosBanco > 10 and Hijos >= 2) or (EstadoCivivl.upper() == "C" and Hijos > 3 and Edad >= 45 and Edad <= 55) or (Ingresos > 2500000 and EstadoCivivl.upper() == "S" and Vivienda.upper() == "U") or (Ingresos > 3500000 and AnnosBanco > 5) or (Vivienda.upper() == "R" and EstadoCivivl.upper() == "C" and Hijos < 2) :
    print("APROBADO")
else:
    print("RECHAZADO")