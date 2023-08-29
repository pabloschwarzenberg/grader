#Ingreso de datos
ingreso = int(input("ingrese su cantidad de ingresos: "))
año = int(input("Ingrese el año de nacimiento: "))
hijos = int(input("Ingrese el numero de hijos: "))
añosbanco = int(input("Ingrese los años de pertenencia al banco: "))
estcivil = input("Ingrese el estado civil (C=Casado/S=Soltero):")
vivienda = input("Ingrese si vive en campo (R) o en ciudad (U): ")

if añosbanco >= 10 and hijos >= 2:
    print("APROBADO")
elif estcivil == "C" and hijos >= 3 and 45 <= 2020-año <= 55:
    print("APROBADO")
elif ingreso >= 2500000 and estcivil == "S" and vivienda == "U":
    print("APROBADO")
elif ingreso >= 3500000 and añosbanco >= 5:
    print("APROBADO")
elif vivienda == "R" and estcivil == "C" and hijos <= 2:
    print("APROBADO")
else:
    print("RECHAZADO")