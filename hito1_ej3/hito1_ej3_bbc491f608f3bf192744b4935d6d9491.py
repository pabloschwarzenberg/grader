#Aprobación de créditos
ingreso = int(input("Ingrese su ingreso en pesos: "))
anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anios_banco = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese si vive en campo (R para rural) o ciudad (U para urbano): ")

if anios_banco > 10 and num_hijos >= 2:
    resultado = "APROBADO"
elif estado_civil == "C" and num_hijos > 3 and anio_nacimiento >= 45 and anio_nacimiento <= 55:
    resultado = "APROBADO"
elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
    resultado = "APROBADO"
elif ingreso > 3500000 and anios_banco > 5:
    resultado = "APROBADO"
elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
    resultado = "APROBADO"
else:
    resultado = "RECHAZADO"

print("Resultado:", resultado)