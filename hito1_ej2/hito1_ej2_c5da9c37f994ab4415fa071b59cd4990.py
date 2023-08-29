#Contestador de celular
telefono = input('Ingrese número de telefono: ')
hora = int(input('Ingrese hora de llamada: '))
code = telefono[5:8]
if 0 <= hora <= 7:
    print('CONTESTAR')
elif hora < 14 and code == '909':
    print('CONTESTAR')
elif hora < 14 :
    print('NO CONTESTAR')
elif 17 <= hora <= 19 and code == '877':
    print('NO CONTESTAR')
elif 17 <= hora == 19:
    print('CONTESTAR')
elif hora > 19:
    print('NO CONTESTAR')
else:
    print('NO CONTESTAR')