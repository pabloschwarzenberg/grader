ingreso = float(input("Ingrese el ingreso mensual en pesos: "))
nacimiento = int(input("Ingrese el año de nacimiento: "))
hijos = int(input("Ingrese el número de hijos: "))
pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese el estado civil (S para soltero, C para casado): ")
lugar_residencia = input("Ingrese el lugar de residencia (U para urbano, R para rural): ")


if pertenencia > 10 and hijos >= 2:
    resultado = "APROBADO"

elif estado_civil == "C" and hijos > 3 and 45 <= (2023 - nacimiento) <= 55:
    resultado = "APROBADO"

elif ingreso > 2500000 and estado_civil == "S" and lugar_residencia == "U":
    resultado = "APROBADO"

elif ingreso > 3500000 and pertenencia > 5:
    resultado = "APROBADO"

elif lugar_residencia == "R" and estado_civil == "C" and hijos < 2:
    resultado = "APROBADO"
    
else:
    resultado = "RECHAZADO"

print(resultado)