# Solicitar datos al cliente
ingreso = float(input("Ingrese el ingreso mensual en pesos: "))
ano_nacimiento = int(input("Ingrese el año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anos_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese el estado civil (S para soltero, C para casado): ")
tipo_vivienda = input("Ingrese el tipo de vivienda (U para urbano, R para rural): ")

# Verificar la aprobación del crédito
aprobado = False

if ingreso >= 3000000 and ano_nacimiento <= 1990:
    aprobado = True
elif num_hijos >= 2 and anos_pertenencia >= 5:
    aprobado = True
elif estado_civil == "C" and tipo_vivienda == "R":
    aprobado = True

# Imprimir el resultado
if aprobado:
    print("APROBADO")
else:
    print("RECHAZADO")
