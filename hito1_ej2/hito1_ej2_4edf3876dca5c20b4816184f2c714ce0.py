#Contestador de celular
telefono= int(input('ingrese numero telefonico: '))
horallamada= int(input('ingrese hora de la llamada: '))

if 10000000 <= telefono <=99999999 and 0 <= horallamada <= 23:

    if horallamada >= 0 and horallamada <= 7:
        print('resultado: CONTESTAR')

    if 8<= horallamada <= 14:
        tresUltimosDigitos = telefono%1000
        if tresUltimosDigitos == 909:
            print('resultado: CONTESTAR')
        else:
            print('resutlado: NO CONTESTAR')
    if 15 <= horallamada <= 17:
        print('resutlado: NO CONTESTAR')
        
    if 18 <= horallamada <= 19:
        tresPrimerosDigitos = telefono//100000

        if tresPrimerosDigitos == 877:
            print('resultado: NO CONTESTAR')
        else:
            print('resultado: CONTESTAR')

    if 19 < horallamada <= 23:
        print('resultado: NO CONTESTAR')
