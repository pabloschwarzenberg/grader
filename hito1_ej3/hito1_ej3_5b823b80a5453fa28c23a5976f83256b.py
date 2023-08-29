#Aprobación de créditos
ingreso = float(input("Ingreso: $"))
nacimiento = int(input("Año de nacimiento: "))
hijos = int(input("Número de hijos: "))
pertenencia = int(input("Años de pertenencia al banco: "))
civil = input("Estado civil (S/C): ")
vive = input("Campo o ciudad (R/U): ")

años = 2020 - nacimiento

if pertenencia > 10 and hijos >= 2:
    print("APROBADO")
elif civil == "C" and hijos > 3 and 45 >= años >= 55:
    print("APROBADO")
elif ingreso > 2500000 and civil == "S" and vive == "U":
    print("APROBADO")
elif ingreso > 3500000 and pertenencia > 5:
    print("APROBADO")
elif vive == "R" and civil == "C" and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")