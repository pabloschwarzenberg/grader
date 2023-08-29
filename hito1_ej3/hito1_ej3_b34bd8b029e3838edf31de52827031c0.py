#Aprobación de créditos
ingreso = int(input("Ingrese el ingreso mensual en pesos: "))
ani = int(input("Ingrese el año de nacimiento: "))
num = int(input("Ingrese el número de hijos: "))
anios = int(input("Ingrese los años de pertenencia al banco: "))
estado = input("Ingrese el estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese la ubicación (U para urbano, R para rural): ")


if anios > 10 and num >= 2:
    print("APROBADO")
elif estado == "C" and num > 3 and anio >= 45 and anio <= 55:
    print("APROBADO")
elif ingreso > 2500000 and estado == "S" and ubicacion == "U":
    print("APROBADO")
elif ingreso > 3500000 and anios> 5:
    print("APROBADO")
elif ubicacion == "R" and estado == "C" and num < 2:
    print("APROBADO")
else:
    print("RECHAZADO")      