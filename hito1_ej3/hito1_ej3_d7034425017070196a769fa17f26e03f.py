#Aprobación de créditos
from time import sleep
ingreso = eval(input("ingrese su ingreso:"))
anio_nacimiento = int(input("ingrese su año de nacimiento:"))
num_h = int(input("ingrese la cantidad de hijos que tiene:"))
anios_banco = int(input("ingresa los años que llevas en el banco:"))
estado_civil = input("(S): soltero, (C), casado:")
vivienda = input("Si vives en ciudad pon (U), si vives en campo po (R):")

while True:
    if anios_banco>10:
        if num_h>=2:
            print("/033[4;42m"+"APROBADO")
            sleep(1)
            break
    if estado_civil=="C":
         if num_h>3:
             if (anio_nacimiento-2020)>=45 and (anio_nacimiento-2020)<=55:
                 print("/033[4;42m"+"APROBADO")
                 sleep(1)
                 break
    if ingreso>2500000:
        if estado_civil=="S":
            if viviendo=="U":
                 print("/033[4;42m"+"APROBADO")
                 sleep(1)
                 break
    if ingreso>3500000:
        if anios_banco>5:
            print("/033[4;42m"+"APROBADO")
            sleep(1)
            break
            
    if vivienda=="R":
        if estado_civil=="C":
            if num_h<3:
                print("/033[4;42m"+"APROBADO")
                sleep(1)
                break
    
    else:
        print("/033[4;41"+"RECHAZADO")
        break
   
           