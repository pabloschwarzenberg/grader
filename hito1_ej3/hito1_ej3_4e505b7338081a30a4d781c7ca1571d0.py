#Aprobación de créditos
# Solicitar datos al cliente
ingreso = int(input("Ingrese el ingreso mensual (en pesos): "))
anio_nacimiento = int(input("Ingrese el año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anios_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese el estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese la ubicación (U para urbano, R para rural): ")

# Verificar aprobación del crédito
if anios_pertenencia > 10 and num_hijos >= 2:
    resultado = "APROBADO"
elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - anio_nacimiento) <= 55:
    resultado = "APROBADO"
elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
    resultado = "APROBADO"
elif ingreso > 3500000 and anios_pertenencia > 5:
    resultado = "APROBADO"
elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
    resultado = "APROBADO"
else:
    resultado = "RECHAZADO"

# Imprimir resultado
print(resultado)   
      