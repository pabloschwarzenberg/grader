#Contestador de celular
telefono = int(input('ingresa un numero telefonico:'))
horallamada = int(input('ingresa hora de la llamada:'))

if 10000000 <= telefono <= 99999999 and 0 <= horallamada <= 23:

    if 0 <= horallamada <= 7:
        print('Resultado: contestar')

    if 8 <= horallamada <= 14:
        tresultimosdigitos = telefono % 1000
        if tresultimosdigitos == 909:
            print('Resultado: contestar')
        else:
            print('Resultado: no contestar')
    if 15 <= horallamada <= 19:
        print('Resultado: no contestar')

    if 17 <= horallamada <= 19:
        primerostresdigitos = telefono // 100000
        if primerostresdigitos == 877:
            print('Resultado: no contestar')
        else:
            print('Resultado: contestar')

    if horallamada > 19:
        print('Resultado: no contestar')

else:
    print('ERROR: telefono u hora de llamada invalido.')
 