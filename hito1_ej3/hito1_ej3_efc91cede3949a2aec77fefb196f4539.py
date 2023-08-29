"""
5.-Un Banco desea implementar una política de atención automatizada de créditos de consumo,
y te contrata para programar su servicio. Los postulantes entregarán al banco la siguiente información:
•	Ingreso (en pesos)
•	Año de nacimiento
•	Número de hijos
•	Años de pertenencia al banco
•	Estado civil ("S": soltero, "C", casado)
•	Si vive en campo o cuidad ("U": urbano, "R": rural)

El banco usará las siguientes reglas para decidir la aprobación del crédito, con una de ellas que se cumpla, se aprueba el crédito:


•	Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
•	Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
•	Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
•	Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
•	Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
Tu programa debe preguntar sus datos al cliente, procesarlos, e imprimir el mensaje APROBADO o
RECHAZADO según corresponda.
"""

ingresos = float(input("Ingresos: "))
año_nacimiento = int(input("Año de nacimiento: "))
numero_hijos = int(input("Número de hijos: "))
apb = int(input("Años de pertenencia al banco: "))
estado_civil = input('Estado civil ("S": soltero, "C": casado): ')
zona = input('En que zona vive ("U": urbano, "R": rural): ')

edad = 2021-año_nacimiento
credito = False #Inicializamos por defecto

if apb > 10 and numero_hijos >= 2:
    credito = True
if estado_civil.lower() == "c" and numero_hijos > 3 and edad >= 45 and edad <= 55:
    credito = True
if ingresos > 2500000 and estado_civil.lower() == "s" and zona.lower() == "u":
    credito = True
if ingresos > 3500000 and apb > 5:
    credito = True
if zona.lower() == "r" and estado_civil.lower() == "c" and numero_hijos < 2:
    credito = True

if credito:
    print("APROBADO")
else:
    print("RECHAZADO")     