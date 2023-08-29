#Aprobación de créditos

from time import sleep
ingreso = eval(input("Ingrese su ingreso:"))
anio_nacimiento = int(input("Ingrese su año de nacimiento:"))
num_h = int(input("Ingrese la cantidad de hijos que tiene:"))
anios_banco = int(input("Ingresa los años que llevas en el banco:"))
estado_civil = input("(S): soltero, (C), casado:")
vivienda = input("Si vivies en ciudad pon (U), si vives en campo pon (R):")

while True:
    if anios_banco>10:
        if num_h>=2:
            print("\033[4;42m"+"APROBADO")
            sleep(1)
            break
    if estado_civil=="C":
        if num_h>3:
            if (anio_nacimiento-2020)>=45 and (anio_nacimiento-2020)<=55:
                print("\033[4;42m"+"APROBADO")
                sleep(1)
                break
    if ingreso>2500000:
        if estado_civil=="S":
            if vivienda=="U":
                print("\033[4;42m"+"APROBADO")
                sleep(1)
                break
    if ingreso>3500000:
        if anios_banco>5:
            print("\033[4;42m"+"APROBADO")
            sleep(1)
            break
    
    if vivienda=="R":
        if estado_civil=="C":
            if num_h<3:
                print("\033[4;42m"+"APROBADO")
                sleep(1)
                break
    
    else:
        print("\033[4;41m"+"RECHAZADO")
        break