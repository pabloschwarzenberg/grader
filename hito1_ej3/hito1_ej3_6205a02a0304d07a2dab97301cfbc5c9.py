#Aprobación de créditos
ingreso = eval(input("Ingrese su ingreso:"))
año_nacimiento = int(input("Ingrese su año de nacimiento:"))
num_h = int(input("Ingrese la cantidad de hijos que tiene:"))
años_banco = int(input("Ingresa los años que llevas en el banco:"))
estado_civil = input("(S): soltero, (C), casado:")
vivienda = input("Si vivies en ciudad pon (U), si vives en campo pon (R):")

while True:
    if años_banco>10:
        if num_h>=2:
            print("APROBADO")
            break
    if estado_civil=="C":
        if num_h>3:
            if (año_nacimiento-2020)>=45 and (año_nacimiento-2020)<=55:
                print("APROBADO")
                break
    if ingreso>2500000:
        if estado_civil=="S":
            if vivienda=="U":
                print(+"APROBADO")
                break
    if ingreso>3500000:
        if años_banco>5:
            print("APROBADO")
            break
    
    if vivienda=="R":
        if estado_civil=="C":
            if num_h<3:
                print("APROBADO")
                break
