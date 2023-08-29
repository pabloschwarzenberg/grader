#Aprobación de créditos
from time import sleep
I = eval(input("Coloque su ingreso mensual (en pesos) -> "))
AN = int(input("Ingrese su año de nacimiento -> "))
NH = int(input("Ingrese el numero de hijos -> "))
AB = int(input("Ingrese los años de antiguedad que lleva en el banco -> "))
EC = input("Si estas soltero coloca -> (S), Si estas casado coloca -> (C)")
VV = input("Si vives en ciudad coloca -> (U), si vives en campo coloca -> (R):")

while True:
    if (AB > 10):
        if (NH >= 2):
            print("\033[4;42m"+"APROBADO")
            sleep(1)
            break

    if (EC == "C"):
        if NH>3:
            if (AN-2020)>=45 and (AN-2020)<=55:
                print("\033[4;42m"+"APROBADO")
                sleep(1)
                break
    
    if I>2500000:
        if EC=="S":
            if VV=="U":
                print("\033[4;42m"+"APROBADO")
                sleep(1)
                break

    if I>3500000:
        if AB>5:
            print("\033[4;42m"+"APROBADO")
            sleep(1)
            break

    if VV=="R":
        if EC=="C":
            if NH<3:
                print("\033[4;42m"+"APROBADO")
                sleep(1)
                break
    else:
        print("\033[4;41m"+"RECHAZADO")
        break
    