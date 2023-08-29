#Contestador de celular
telefono = int(input('Ingrese numero telefonico: '))
horaLlamada = int(input('Ingrese hora de la llamada: '))

if 10000000 <= telefono <= 99999999 and 0 <= horaLlamada <= 23:

    # CONDICION 1:
    ## Si la llamada ocurre entre 00:00 y 07:00,
    ## la contestas ya que podría ser una emergencia.

    # if horaLlamada >= 0 and horaLlamada <= 7:
    
    if 0 <= horaLlamada <= 7:
        print('Resultado: CONTESTAR')

    # CONDICION 2:
    ## Si ocurre antes de las 14:00 no la contestas,
    ## excepto si el número termina en 909.
        
    if 7 < horaLlamada <= 14:
        tresUltimosDigitos = telefono%1000 #Con % consigo los últimos digitos!!!
        if tresUltimosDigitos == 909:
            print('Resultado: CONTESTAR')
        else:
            print('Resultado: NO CONTESTAR')

    # CONDICION 3:        
    ## Durante la tarde, solamente contestas entre 17:00 y 19:00,
    ## exceptuando un número que comienza por 877.
    if 14 < horaLlamada < 17:
        print('Resultado: NO CONTESTAR')

    if 17 <= horaLlamada <= 19:
        tresPrimerosDigitos = telefono//100000 #Con // le sacas digitos al número
        if tresPrimerosDigitos == 877:
            print('Resultado: NO CONTESTAR')
        else:
            print('Resultado: CONTESTAR')            

    # CONDICION 4:                                          
    ## Después de las 19:00, no contestas el celular.
    if 19 < horaLlamada <= 23:
        print('Resultado: NO CONTESTAR')

else:
    print('Al menos uno de los datos ingresados NO ES VÁLIDO!')