#Aprobación de créditos
# Solicitar al cliente que ingrese la información requerida
ingreso = int(input("Ingrese su ingreso en pesos: "))
ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anos_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
lugar_residencia = input("Ingrese si vive en campo (R) o ciudad (U): ")

# Verificar las reglas para aprobar el crédito
aprobado = False

if anos_pertenencia > 10 and num_hijos >= 2:
    aprobado = True
elif estado_civil == "C" and num_hijos > 3 and ano_nacimiento >= 45 and ano_nacimiento <= 55:
    aprobado = True
elif ingreso > 2500000 and estado_civil == "S" and lugar_residencia == "U":
    aprobado = True
elif ingreso > 3500000 and anos_pertenencia > 5:
    aprobado = True
elif lugar_residencia == "R" and estado_civil == "C" and num_hijos < 2:
    aprobado = True

# Imprimir el resultado de la aprobación del crédito
if aprobado:
    print("APROBADO")
else:
    print("RECHAZADO")
      