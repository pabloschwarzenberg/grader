#Aprobación de créditos
ingreso = int(input("Ingrese su ingreso en pesos: "))
anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anios_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
residencia = input("Ingrese si vive en campo (R) o ciudad (U): ")

# Verificar si se aprueba el crédito según las reglas establecidas
if (anios_pertenencia > 10 and num_hijos >= 2) or \
   (estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - anio_nacimiento) <= 55) or \
   (ingreso > 2500000 and estado_civil == "S" and residencia == "U") or \
   (ingreso > 3500000 and anios_pertenencia > 5) or \
   (residencia == "R" and estado_civil == "C" and num_hijos < 2):
    resultado = "APROBADO"
else:
    resultado = "RECHAZADO"

print("El resultado de la evaluación es:", resultado)
      