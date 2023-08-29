ingreso = float(input("Ingrese su ingreso en pesos: "))
ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos que tiene: "))
anos_banco = int(input("Ingrese los años que lleva perteneciendo al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
vive_en = input("Ingrese si vive en campo o ciudad (U para urbano, R para rural): ")

if anos_banco > 10 and num_hijos >= 2:
    print("APROBADO")
elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - ano_nacimiento) <= 55:
    print("APROBADO")
elif ingreso > 2500000 and estado_civil == "S" and vive_en == "U":
    print("APROBADO")
elif ingreso > 3500000 and anos_banco > 5:
    print("APROBADO")
elif vive_en == "R" and estado_civil == "C" and num_hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")