#Aprobación de créditos
ingreso = int(input("Ingrese su ingreso en pesos: "))
anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anios_banco = int(input("Ingrese años de pertenencia al banco: "))
estado_civil = input("Ingrese estado civil (S=soltero, C=casado): ")
ubicacion = input("Ingrese ubicación (U=urbano, R=rural): ")

if anios_banco > 10 and num_hijos >= 2:
    print("APROBADO")
elif estado_civil == "C" and num_hijos > 3 and anio_nacimiento >= 45 and anio_nacimiento < 55:
    print("APROBADO")
elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
    print("APROBADO")
elif ingreso > 3500000 and anios_banco > 5:
    print("APROBADO")
elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
      