from time import sleep
peso = eval(input("Ingrese su ingreso:"))
nacimiento = int(input("Ingrese su año de nacimiento:"))
hijos = int(input("Ingrese la cantidad de hijos que tiene:"))
banco = int(input("Ingresa los años que llevas en el banco:"))
civil_estado = input("(S): soltero, (C), casado:")
campo_ciudad = input("Si vivies en ciudad pon (U), si vives en campo pon (R):")

while True:
    if banco>10:
        if hijos>=2:
            print("\033[4;42m"+"APROBADO")
            sleep(1)
            break
    if civil_estado=="C":
        if hijos>3:
            if (nacimiento-2020)>=45 and (nacimiento-2020)<=55:
                print("\033[4;42m"+"APROBADO")
                sleep(1)
                break
    if peso>2500000:
        if civil_estado=="S":
            if campo_ciudad=="U":
                print("\033[4;42m"+"APROBADO")
                sleep(1)
                break
    if peso>3500000:
        if banco>5:
            print("\033[4;42m"+"APROBADO")
            sleep(1)
            break
    
    if campo_ciudad=="R":
        if civil_estado=="C":
            if hijos<3:
                print("\033[4;42m"+"APROBADO")
                sleep(1)
                break
    
    else:
        print("\033[4;41m"+"RECHAZADO")
        break