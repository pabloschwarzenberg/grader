telefono = int(input('Ingrese numero telefonico: '))
hora = int(input('Ingrese hora de la llamada: '))

## número mas chico q puedo escribir con 8 cifras: 10000000 (si le resto 1: 9999999)
## número mas grande q puedo escribir con 8 cifras: 99999999 (si le sumo 1: 100000000)

if 10000000 <= telefono <= 99999999 and 0 <= hora <= 23:

    ## COND1: Si la llamada ocurre entre 00:00 y 07:00,
    ## la contestas ya que podría ser una emergencia.
    ## if hora >= 0 and hora <= 7: (TAMBIÉN SIRVE)

    if 0 <= hora <= 7:
        print('Resultado: CONTESTAR')

    ## COND2: Si la llamada ocurre antes de las 14:00
    ## no la contestas, excepto si el número termina en 909.

    if 7 < hora < 14:

        tresUltimosDigitos = telefono%1000 ## Con % consigo los ultimos digitos

        if tresUltimosDigitos == 909:
            print('Resultado: CONTESTAR')
        else: 
            print('Resultado: NO CONTESTAR')

    ## COND3: Durante la tarde, solamente contestas entre 17:00 y 19:00,
    ## exceptuando un número que comienza por 877.

    if 14 <= hora < 17:
        print('Resultado: NO CONTESTAR')

    if 17 <= hora <= 19:

        tresPrimerosDigitos = telefono//100000 ## Con // obtengo el numero sin los 5 digitos de la derecha

        if tresPrimerosDigitos == 877:
            print('Resultado: NO CONTESTAR')
        else:
            print('Resultado: CONTESTAR')

    ## COND4: Después de las 19:00, no contestas el celular.
    if 19 < hora <= 23:
        print('Resultado: NO CONTESTAR')

else:
    print('Alguno de los valores ingresados')