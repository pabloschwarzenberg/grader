#Contestador de celular
telefono = int(input('ingresa numero telefonico:' ))
horallamada = int(input('ingresa hora de llamada:' ))

if 10000000 <= telefono <= 99999999 and 0 <= horallamada <= 23:
    if 0 <= horallamada <= 7:
        print('resultado: CONTESTAR')

    if 8 <= horallamada <= 14:
        TresUltimosDigitos = telefono%1000
        if TresUltimosDigitos == 909:
            print('resultado: CONTESTAR')
        else:
            print('resultado: NO CONTESTAR')
            
    if 15 <= horallamada <=16:
        print('resultado: NO CONTESTAR')

    if 17 <= horallamada <= 19:
        TresPrimerosDigitos = telefono//100000
        if TresPrimerosDigitos == 877:
            print('resultado: NO CONTESTAR')
        else:
            print('resultado: CONTESTAR')
            
    if 20 <= horallamada <= 23:
        print('resultado: NO CONTESTAR')
           
        
else:
     print('uno o mas de los datos son invalidos')      