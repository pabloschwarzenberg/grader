ingreso = int(input("Ingrese su ingreso en pesos: "))
año_nacimiento = int(input("Ingrese su año de nacimiento: "))
numero_hijos = int(input("Ingrese el número de hijos: "))
años_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
lugar_residencia = input("Ingrese su lugar de residencia (U para urbano, R para rural): ")
if años_pertenencia > 10 and numero_hijos >= 2:
    print("APROBADO")
elif estado_civil == "C" and numero_hijos > 3 and 45 <= (2023 - años_nacimiento) <= 55:
    print("APROBADO")
elif ingreso > 2500000 and estado_civil == "S" and lugar_residencia == "U":
    print("APROBADO")
elif ingreso > 3500000 and años_pertenencia > 5:
    print("APROBADO")
elif lugar_residencia == "R" and estado_civil == "C" and numero_hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
