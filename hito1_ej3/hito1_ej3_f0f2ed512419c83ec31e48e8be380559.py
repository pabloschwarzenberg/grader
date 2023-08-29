#Aprobación de créditos
ingresos = int(input("ingrese ingresos en pesos: "))
year_de_nacimiento = int(input("ingrese año de nacimiento: "))
hijos = int(input("ingrese numero de hijos: "))
pertenencia = int(input("ingrese años de pertenencia al banco: "))
estado = input("ingrese estado civil, S = soltero o C = casado: ")
vive = input("ingrese U si vive en ciudad y R si vive en campo ")

year = year_de_nacimiento - 2021
if pertenencia > 10 and hijos >= 2:
    print("APROBADO")
else:
    print("RECHAZADO")
if estado == "C" and hijos > 3 and year_de_nacimiento > 45 < 55:
    print("APROBADO")
else:
    print("RECHAZADO")
if ingresos > 2500000 and estado == "S" and vive == "U":
    print("APROBADO")
else:
    print("RECHAZADO")
if ingresos > 3500000 and pertenencia > 5:
    print("APROBADO")
else:
    print("RECHAZADO")
if vive == "R" and estado == "C" and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
