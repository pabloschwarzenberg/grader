ingreso = eval(input("Ingrese sus ingresos:"))
edad = int(input("su año de nacimiento?:"))
familia= int(input("cuantos hijos tienes?:"))
cliente = int(input("Ingresa los años que llevas en el banco:"))
estado_civil = input("(S): soltero, (C), casado:")
lugar = input("Si vivies en ciudad pon (U), si vives en campo pon (R):")

while True:
    if cliente>10:
        if familia>=2:
            print("\033[4;42m"+"APROBADO")
            
            break
    if estado_civil=="C":
        if familia>3:
            if (edad-2020)>=45 and (edad-2020)<=55:
                print("\033[4;42m"+"APROBADO")
                
                break
    if ingreso>2500000:
        if estado_civil=="S":
            if lugar=="U":
                print("\033[4;42m"+"APROBADO")
                
                break
    if ingreso>3500000:
        if cliente>5:
            print("\033[4;42m"+"APROBADO")
            
            break
    
    if lugar=="R":
        if estado_civil=="C":
            if familia<3:
                print("\033[4;42m"+"APROBADO")
                
                break
    
    else:
        print("\033[4;41m"+"RECHAZADO")
        break

 