#Contestador de celular
telefono = int(input('Ingrese numero telefonico: '))
horaLlamada = int(input('ingrese hora de la llamada: '))

if 10000000 <= telefono <= 99999999 and 0 <= horaLlamada <= 23:

    if 0 <= horaLlamada <= 7:
        print('Resultado: CONTESTAR')
    
    if 8 <= horaLlamada <= 14:
        TresultimosDigitos = telefono%1000
        if TresultimosDigitos == 909:
            print('Resultado: CONTESTAR')
        else:
            print('Resultado: NO CONTESTAR')

    if 15 <= horaLlamada <= 16:
        print('Resultado: NO CONTESTAR')

    if 17 <= horaLlamada <= 19:
        tresPrimerosDigitos = telefono//10000
        if tresPrimerosDigitos == 877:
            print('Resultado: CONTESTAR')
        else:
            print('Resultado: NO CONTESTAR')

    if 20 <= horaLlamada <= 23:
        print('Resultado: NO CONTESTAR')

else:
    print('Uno o mas de los datos ingresados son invalidos.')