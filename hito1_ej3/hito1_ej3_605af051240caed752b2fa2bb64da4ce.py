#Aprobación de créditos
ingreso = int(input("Ingrese el ingreso en pesos: "))
ano_nacimiento = int(input("Ingrese el año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anos_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese el estado civil (S para soltero, C para casado): ")
lugar_residencia = input("Ingrese el lugar de residencia (U para urbano, R para rural): ")

if anos_pertenencia > 10 and num_hijos >= 2:
    print("APROBADO")
elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - ano_nacimiento) <= 55:
    print("APROBADO")
elif ingreso > 2500000 and estado_civil == "S" and lugar_residencia == "U":
    print("APROBADO")
elif ingreso > 3500000 and anos_pertenencia > 5:
    print("APROBADO")
elif lugar_residencia == "R" and estado_civil == "C" and num_hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
      