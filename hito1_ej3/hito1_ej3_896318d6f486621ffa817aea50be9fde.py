#Aprobación de créditos
pesos = int(input("Ingresos (pesos): "))
nacimiento = int(input("Año de nacimiento: "))
hijos = int(input("Numero de hijos: "))
pertenencia = int(input("Años de pertenencia al banco: "))
Estado_civil = str(input("Ingrese si es Soltero (S) o Casado (C): "))
vivienda = str(input("Ingrese si vive en campo (R) o ciudad (U): "))

AñoActual = 2022
Edad = AñoActual - nacimiento


if pertenencia > 10 and hijos >= 2:
    print("APROBADO")

if str(Estado_civil) == "C" and hijos > 3 and nacimiento > 45  and nacimiento < 55:
    print ("APROBADO")

if pesos > 2500000 and Estado_civil == "S" and vivienda == "U":
    print ("APROBADO")

if pesos > 3500000 and pertenencia > 5:
    print("APROBADO")

if vivienda == "R" and Estado_civil == "C" and hijos < 2:
    print("APROBADO")

else:
    print("RECHAZADO")