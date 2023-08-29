#Contestador de celular
telefono = int(input('Ingrese número telefónico: '))
hora = int(input('Ingrese hora de la llamada: '))

if hora >= 0 and hora <= 7:
    print('Resultado: CONTESTAR')
elif hora > 7 and hora <= 24:
    if telefono%10**3 == 909:
        print('Resultado: CONTESTAR')
    else:
        print('Resultado: NO CONTESTAR')
elif hora >= 17 and hora <= 19:
    if telefono%10**3 == 877:
        print('Resultado: CONTESTAR')
    else:
        print('Resultado: NO CONTESTAR')
elif hora > 19 and hora <= 23:
    print('Resultado_ NO CONTESTAR')
else:
    print('Resultado: NO CONTESTAR')