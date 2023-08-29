#Aprobación de créditos

from time import sleep
ingreso = eval(input("Introduzca su ingreso:"))
ano_nacimiento = int(input("Ingrese su año de nacimiento:"))
hijos = int(input("Ingrese la cantidad de hijos que tiene:"))
anos_banco = int(input("Ingresa los años que llevas en el banco:"))
estado_civil = input("(S): soltero, (C), casado:")
vivienda = input("Si vivies en ciudad pon (U), si vives en campo pon (R):")

while True:
    if anos_banco>10:
        if hijos>=2:
            print("\033[4;42m"+"APROBADO")
            sleep(1)
            break
    if estado_civil=="C":
        if hijos>3:
            if (ano_nacimiento-2020)>=45 and (ano_nacimiento-2020)<=55:
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
        if anos_banco>5:
            print("\033[4;42m"+"APROBADO")
            sleep(1)
            break
    
    if vivienda=="R":
        if estado_civil=="C":
            if hijos<3:
                print("\033[4;42m"+"APROBADO")
                sleep(1)
                break
    
    else:
        print("\033[4;41m"+"RECHAZADO")
        break    