#Contestador de celular
telefono = int(input(' Ingrese numero telefonico: '))
horaLlamada = int(input(' Ingrese hora de la llamada: '))

if 10000000<= telefono <= 99999999 and 0 <= horaLlamada <= 23:

    if 0<= horaLlamada <=7:
        print('Reultado: NO CONTESTAR')

    if 8 <= horaLlamada <= 14:
        tresUltimosDigitos = telefono %1000
        if tresUltimosDigitos == 909: 
            print('Resultado: CONTESTAR ')
        else:
            print(' Resultado: NO CONTESTAR')

    if 15<= horaLlamada <=19:
        tresPrimerosDigitos = telefono//100000
        if tresPrimerosDigitos == 877:
            print('Resultado: NO CONTESTAR')
        else:
            print('Resultado: CONTESTAR')
            
    if 19<= horaLlamada <= 23:
        print('Resultado: NO CONTESTAR')
else:
    print('ERROR: Telefono u Hora de Llamada inválidos.')