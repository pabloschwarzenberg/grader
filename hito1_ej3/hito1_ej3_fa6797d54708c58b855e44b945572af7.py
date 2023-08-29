ingreso = eval(input('¿Cual fue tu ingreso?: '))
nacimiento = eval(input('¿Año de nacimiento?: '))
hijos = eval(input('¿Numero de hijos?: '))
anosperbanco = eval(input('¿Años de pertenencia al banco?: '))
estado = input('¿Estado civil?("S": soltero, "C", casado): ')
hogar = input('¿Vives en campo o ciudad?("U": urbano, "R": rural): ')

edad = 2020 - nacimiento

if hijos >= 2 and anosperbanco > 10:
    print('APROBADO') 
else:
    print('RECHAZADO')

    if estado ==  "C" and hijos > 3 and edad > 45 < 55:
        print('APROBADO')
    else:
        print('RECHAZADO')

    if ingreso > 2500000 and estado == "S" and hogar == "U":
        print('APROBADO')
    else:
        print('RECHAZADO')
    

    if ingreso > 3500000 and anosperbanco < 5:
        print('APROBADO')
    else:
        print('RECHAZADO')

    if hogar == "R" and estado == "C" and hijos > 0 < 2:
        print('APROBADO')
    else:
        print('RECHAZADO')
