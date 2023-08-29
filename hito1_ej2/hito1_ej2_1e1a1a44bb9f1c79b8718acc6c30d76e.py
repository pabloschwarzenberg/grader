#Contestador de celular
#control ej 4
#Escribe un programa para contestar automáticamente el celular, dependiendo de la hora en que llega la llamada y el número de teléfono. El número telefónico debe ser representado por un número entero (int) de 8 cifras, mientras que la hora es representada por un número entero entre 0 y 23. Las reglas que rigen si contestarás o no son las siguientes:
#Si la llamada ocurre entre 00:00 y 07:00, la contestas ya que podría ser una emergencia.
#Si ocurre antes de las 14:00 no la contestas, excepto si el número termina en 909.
#Durante la tarde, solamente contestas entre 17:00 y 19:00, exceptuando un número que comienza por 877.
#Después de las 19:00, no contestas el celular.
#El programa debe preguntar al usuario por la hora del día y por el número de celular que llama, e imprimir “CONTESTAR” o “NO CONTESTAR” en pantalla.
#
#Ejemplo 1
#>>> Ingrese numero telefonico: 77389909
#>>> Ingrese hora de la llamada: 13
#>>> Resultado: CONTESTAR
#Ejemplo 2
#>>> Ingrese numero telefonico: 98927674
#>>> Ingrese hora de la llamada: 20
#>>> Resultado: NO CONTESTAR
#Ejemplo 3
#>>> Ingrese numero telefonico: 87765545
#>>> Ingrese hora de la llamada: 18
#>>> Resultado: NO CONTESTAR

telefono = int(input('Ingrese numero telefonico: '))
horaLlamada = int(input('Ingrese hora de la llamada: '))


if 10000000 <= telefono <= 99999999 and 0 <= horaLlamada <= 23:
    


    if 0 <= horaLlamada <= 7:
        print('Resultado: CONTESTAR')



    if 8 <= horaLlamada <= 14:
        tresUltimosDigitos = telefono % 1000  
        if tresUltimosDigitos == 909:
            print('Resultado: CONTESTAR')
        else:
            print('Resultado: NO CONTESTAR')



    if 15 <= horaLlamada <= 16:
        print('Resultado: NO CONTESTAR')

    if 17 <= horaLlamada <= 19:          
        tresPrimerosDigitos = telefono //100000   
        if tresPrimerosDigitos == 877:
            print('Resultado: NO CONTESTAR')
        else:
            print('Resultado: CONTESTAR')

    if 20 <= horaLlamada <= 23:          
        print('Resultado: NO CONTESTAR')

else:
    print('ERROR: Teléfono u Hora de Llamada inválidos.')
     