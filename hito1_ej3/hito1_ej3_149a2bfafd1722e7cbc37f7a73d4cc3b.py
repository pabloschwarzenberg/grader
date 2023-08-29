#Aprobación de créditos
ingreso = int(input("Ingrese el ingreso mensual en pesos: "))
nacimiento = int(input("cuando nacio: "))
num_hijos = int(input("Ingrese el numero de hijos: "))
pertenencia = int(input("Ingrese el tiempo de pertenencia en el banco: "))
estado_civil = input("Ingrese el estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese la ubicacion (U para urbano, R para rural): ")

# Verificar las reglas para aprobar el credito
if pertenencia > 10 and num_hijos >= 2:
    print("APROBADO")
elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - nacimiento) <= 55:
    print("APROBADO")
elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
    print("APROBADO")
elif ingreso > 3500000 and pertenencia > 5:
    print("APROBADO")
elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
   