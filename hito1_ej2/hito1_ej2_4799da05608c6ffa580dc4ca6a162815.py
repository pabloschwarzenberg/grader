#Contestador de celular
telefono = int(input('Ingrese numero telefonico:'))
horaLlamada = int(input('Ingrese hora de la llamada:'))
if 0 <= horaLlamada <= 7:
    print('Resultado: CONTESTAR')
    
if 8 <= horaLlamada <= 14:
        tresUltimosDigitos = telefono%1000
        if tresUltimosDigitos == 909:
            print('Resultado: CONTESTAR')
        else:
            print('Resultado: NO CONTESTAR')

if 15 <= horaLlamada <= 16:
    print('Resultado: NO CONTESTAR')

if 17 <= horaLlamada <= 19:
     tresPrimerosDigitos = telefono//100000
     if tresPrimerosDigitos == 877:
          print('Resultado: NO CONTESTAR')
     else:
         print('Resultado: CONTESTAR')

if 20 <= horaLlamada <= 23:
    print('Resultado: NO CONTESTAR')    