#Contestador de celular
numero=(input('ingrese numero de 8 cifras: '))
hora=int(input('Ingrese hora de la llamada: '))
if hora <= 7:
    print('CONTESTAR')
elif hora <14:
    if numero[-3:]=='909':
        print('CONTESTAR')
    else:
        print('NO CONTESTAR')
elif 17<=hora<=19:
    if numero[:3]=='877':
        print('NO CONTESTAR')
    else:
        print('CONTESTAR')
elif hora>19:
     print('NO CONTESTAR')      