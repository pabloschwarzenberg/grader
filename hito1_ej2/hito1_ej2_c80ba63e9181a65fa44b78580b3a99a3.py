#Contestador de celular
num_telefonico = int(input('Ingrese número telefónico: '))
hora = int(input('Ingrese hora de la llamada: '))
if hora >= 0 and hora < 7:
    print('CONTESTAR')
elif hora > 7 and hora <14 and str(num_telefonico)[-3:] == '909':
    print('CONTESTAR')
elif hora > 7 and hora <14:
    print('NO CONTESTAR')
elif hora > 14 and hora < 17:
    print('NO CONTESTAR')
elif hora >= 17 and hora <19 and str(num_telefonico)[:3] == '877':
    print('NO CONTESTAR')
elif hora >= 17 and hora < 19:
    print('CONTESTAR')
elif hora > 19:
    print('NO CONTESTAR')      