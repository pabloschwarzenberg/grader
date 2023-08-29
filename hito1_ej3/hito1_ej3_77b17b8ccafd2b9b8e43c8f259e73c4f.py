'''
Un Banco desea implementar una política de atención automatizada de créditos de consumo, y te contrata para programar su servicio. Los postulantes entregarán al banco la siguiente información:

Ingreso (en pesos)
Año de nacimiento
Número de hijos
Años de pertenencia al banco
Estado civil ("S": soltero, "C", casado)
Si vive en campo o cuidad ("U": urbano, "R": rural)

El banco usará las siguientes reglas para decidir la aprobación del crédito, con una de ellas que se cumpla, se aprueba el crédito:

Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
Tu programa debe preguntar sus datos al cliente, procesarlos, e imprimir el mensaje APROBADO o RECHAZADO según corresponda.
'''

ingreso = int(input("Ingrese sus ingresos (en pesos): "))
year_nacimiento = int(input("Ingrese el año de su nacimiento: "))
n_hijo = int(input("Ingrese el numero de hijos que tiene: "))
pertenencia = int(input("Ingrese los años que lleva en el banco: "))
estado_civil = str(input("Ingrese estado civil soltero (S) o casado (C): "))
sector = str(input("Ingrese lugar de residencia urbano (U) o rural (R): "))

year_act = 2021
resultado = "RECHAZADO"
edad = year_act - year_nacimiento
if(pertenencia > 10 and n_hijo >= 2):
    resultado = "APROBADO"
elif(estado_civil == "C" and n_hijo > 3 and edad >= 45 and edad <= 55):
    resultado = "APROBADO"
elif(ingreso > 2500000 and estado_civil == "S" and sector == "U"):
    resultado = "APROBADO"
elif(ingreso > 3500000 and pertenecia > 5):
    resultado = "APROBADO"
elif(estado_civil == "C" and n_hijo < 2):
    resultado = "APROBADO"
print(resultado)