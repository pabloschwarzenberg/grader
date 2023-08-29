Num = int(input('Ingrese número telefonico: '))
hora = int(input('Ingrese hora de la llamada: '))
NumList = list(str(Num))
if 0 <= hora <= 7:
    print('CONTESTAR')

elif hora > 19:
    print('NO CONTESTAR')

elif hora < 14 and NumList[-3:] == ['9', '0', '9']:
    print('CONTESTAR')

elif 17 <= hora <= 19:
    if NumList[:3] == ['8','7','7']:
        print('NO CONTESTAR')
    else:
        print('CONTESTAR')
else:
    print('NO CONTESTAR')

