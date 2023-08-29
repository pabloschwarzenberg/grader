#Un Banco desea implementar una política de atención automatizada de créditos de consumo, y te contrata para programar su servicio. Los postulantes entregarán al banco la siguiente información:

#Ingreso (en pesos)
#Año de nacimiento
#Número de hijos
#Años de pertenencia al banco
#Estado civil ("S": soltero, "C", casado)
#Si vive en campo o cuidad ("U": urbano, "R": rural)

#El banco usará las siguientes reglas para decidir la aprobación del crédito, con una de ellas que se cumpla, se aprueba el crédito:

#Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
#Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
#Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
#Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
#Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
#Tu programa debe preguntar sus datos al cliente, procesarlos, e imprimir el mensaje APROBADO o RECHAZADO según corresponda.

from os import system
system("cls")
print("Ingrese datos del cliente.")

ingreso=int(input("Indique su ingreso total en pesos: "))
nacimiento=int(input("Ingrese su año de nacimiento: "))
n_hijos=int(input("Ingrese su numero de hijos: "))
a_cliente=int(input("Ingrese cuantos años a sido cliente de nuestro banco: "))
e_civil=input("Indique si usted vive es soltero [S] o casado [C]: ")
camp_cit=input("Indique si usted vive en el campo [R] o en ciudad [U]: ")
credito = "RECHAZADO"
edad = 2023 - nacimiento

while True:
    if e_civil.lower() == "c" or e_civil.lower() == "s":
        break
    else:
        e_civil = input("Indique si usted es soltero con una [S] o casado con una [C]: ")

while True:
    if camp_cit.lower() == "r" or camp_cit.lower() == "u":
        break
    else:
        camp_cit = input("Indique si usted vive en el campo con una [R] o en ciudad con una [U]: ")

if a_cliente > 10 and n_hijos >= 2:
    credito = "APROBADO"

if e_civil.lower() == "c" and n_hijos > 3 and 45 <= edad <= 55:
    credito = "APROBADO"

if ingreso >= 2500000 and e_civil.lower() == "s" and camp_cit.lower() == "u":
    credito = "APROBADO"

if ingreso >= 3500000 and a_cliente > 5:
    credito = "APROBADO"

if camp_cit.lower() == "r" and e_civil.lower() == "c" and n_hijos < 2:
    credito = "APROBADO"

print("---------------------------------------------------------\nSu crédito fue",credito)
print(credito)