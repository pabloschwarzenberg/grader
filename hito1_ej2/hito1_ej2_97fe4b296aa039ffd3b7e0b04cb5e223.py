#Contestador de celular

telefono=eval(input('Ingresa tu numero de telefono: '))
horadellamada=eval(input('Ingresa la hora de llamada: '))

if 11111111 <= telefono <= 99999999 and 0 <= horadellamada <= 23:
    if 0 <= horadellamada <= 7:
        print('Resultado: Contestar')
    if 8 <= horadellamada <= 14:
        tresultimosdigitos = telefono%1000
        if tresultimosdigitos == 909:
            print('Resultado: CONTESTAR')
        else:
            print('Resultado: NO CONTESTAR')
    if 15 <= horadellamada <= 16:
        print('Resultado: NO CONTESTAR')
    if 17 <= horadellamada <= 19:
        tresprimerosdigitos=telefono//100000
        if tresprimerosdigitos == 877:
            print('Resultado: NO CONTESTAR')
        else:
            print('Resultado: CONTESTAR')
    if 19 <= horadellamada <= 23:
        print('Resultado: NO CONTESTAR')

else:
    print('Error: Telefono u horadellamada invalidos')
    
