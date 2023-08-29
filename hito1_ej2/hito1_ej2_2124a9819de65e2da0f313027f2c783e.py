#Contestador de celular
numero = input('ingrese numero telefonico: ')
hora = int(input('ingrese hora de la llamada: '))
if hora >= 0 and hora <= 7:
    print('CONTESTAR')
elif hora <14:
    if numero[-3]=='909':
        print('CONTESTAR')
    else:
        print('NO CONTESTAR')
elif hora >= 17 and hora <=19:
    if numero[:3]=='877':
        print('CONTESTAR')
    else:
        print('CONTESTAR')
elif hora >=19:
     print('NO CONTESTAR')