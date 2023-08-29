#Aprobación de créditos
ingreso = int(input("Ingreso mensual (en pesos): "))
anio_nacimiento = int(input("Año de nacimiento: "))
num_hijos = int(input("Número de hijos: "))
anios_pertenencia = int(input("Años de pertenencia al banco: "))
estado_civil = input("Estado civil (S para soltero, C para casado): ")
ubicacion = input("Ubicación (U para urbano, R para rural): ")

if anios_pertenencia > 10 and num_hijos >= 2:
    print("APROBADO")
elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - anio_nacimiento) <= 55:
    print("APROBADO")
elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
    print("APROBADO")
elif ingreso > 3500000 and anios_pertenencia > 5:
    print("APROBADO")
elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")      