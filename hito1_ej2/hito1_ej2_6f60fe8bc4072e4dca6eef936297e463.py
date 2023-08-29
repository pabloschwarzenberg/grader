#Contestador de celular
telefono = int(input('Ingrese numero telefonico: '))
horaLlamada = int(input('Ingrese hora de la llamada: '))


if 10000000 <= telefono <= 99999999 and 0 <= horaLlamada <= 23:
    
    ## PRIMERA CONDICIÓN:
    # Si la llamada ocurre entre 00:00 y 07:00,
    # la contestas ya que podría ser una emergencia.

    if 0 <= horaLlamada <= 7:          ## ES LO MISMO QUE: if horaLlamada >= 0 and horaLlamada <= 7:
        print('Resultado: CONTESTAR')

    ## SEGUNDA CONDICIÓN:
    ## Si ocurre antes de las 14:00 no la contestas,
    ## excepto si el número termina en 909.

    if 8 <= horaLlamada <= 14:
        tresUltimosDigitos = telefono % 1000   ## SIEMPRE OBTENDRÁS LOS 3 ÚLTIMOS DÍGITOS!!!!
        if tresUltimosDigitos == 909:
            print('Resultado: CONTESTAR')
        else:
            print('Resultado: NO CONTESTAR')

    ## TERCERA CONDICIÓN:
    ## Durante la tarde, solamente contestas entre 17:00 y 19:00,
    ## exceptuando un número que comienza por 877.

    if 15 <= horaLlamada <= 16:
        print('Resultado: NO CONTESTAR')

    if 17 <= horaLlamada <= 19:          
        tresPrimerosDigitos = telefono //100000   ## SIEMPRE LE SACA LOS ÚLTIMOS 5 DIGITOS: POR ESO TE QUEDAS CON 3
        if tresPrimerosDigitos == 877:
            print('Resultado: NO CONTESTAR')
        else:
            print('Resultado: CONTESTAR')

    ## CUARTA CONDICIÓN:
    ## Después de las 19:00, no contestas el celular.    
    if 20 <= horaLlamada <= 23:          
        print('Resultado: NO CONTESTAR')

else:
    print('ERROR: Teléfono u Hora de Llamada inválidos.')