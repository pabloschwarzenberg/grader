#Contestador de celular
telefono = int(input('ingrese un numero : '))
hora = int(input('ingrese la hora'))

if 10000000 <= telefono <= 99999999 and 0 <= hora <= 23:

    if hora >= 0 and hora <= 7 :
        print('resultado: contestar')

    if 7 < hora <= 14 :
        tresUltimosDigitos=telefono%1000
        if tresUltimosDigitos == 909:
            print('resultado: contestar')
        else:
            print('resultado: no contestar')

    if 14 < hora < 17 :
        print('resultado: no contestar')

    if 17 <= hora <=19:
        tresPrimerosDigitos = telefono//100000
        if tresPrimerosDigitos == 877:
            print('resultado: no contestar')
        else:
            print('resultado: contestar')

    if 19 < hora <= 23:
        print('resultado: no contestar')

else:
    print('al menos uno de los datos ingresados no es valido')
