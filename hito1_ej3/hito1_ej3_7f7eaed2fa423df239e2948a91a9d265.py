#Aprobación de créditos
from time import sleep
ingreso = eval(input("Registre su ingreso:"))
nacimiento = int(input("Registre su año de nacimiento:"))
hijos = int(input("Registre cantidad de hijos:"))
tiempo_banco = int(input("Registre años que lleva en el banco:"))
estado_civil = input("Digite (S) para soltero o (C) para casado:")
vivienda = input("Si vives en ciudad digita (U), si vives en campo digita (R):")

while True:
    if tiempo_banco>10:
        if hijos>=2:
            print("\033[4;42m"+"APROBADO")
            sleep(1)
            break
    if estado_civil=="C":
        if hijos>3:
            if (nacimiento-2020)>=45 and (nacimiento-2020)<=55:
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
        if tiempo_banco>5:
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

