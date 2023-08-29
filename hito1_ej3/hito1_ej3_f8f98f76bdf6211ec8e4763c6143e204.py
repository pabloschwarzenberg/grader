#Aprobación de créditos
ingreso = float(input("Ingrese su ingreso en pesos: "))
nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
vivienda = input("Ingrese si vive en campo o ciudad (U para urbano, R para rural): ")

if pertenencia > 10 and num_hijos >= 2:
    print("APROBADO")
elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - nacimiento) <= 55:
    print("APROBADO")
elif ingreso > 2500000 and estado_civil == "S" and vivienda == "U":
    print("APROBADO")
elif ingreso > 3500000 and pertenencia > 5:
    print("APROBADO")
elif vivienda == "R" and estado_civil == "C" and num_hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")      