numero=0
hora=-1
while len(str(numero)) != 8:
    numero=int(input('Ingrese numero telefónico: '))
while hora<0 or hora>23:
    hora=int(input('Ingrese hora de la llamada: '))
if hora >=0 and hora < 7:
    print('CONTESTAR')
elif hora >=7 and hora < 14:
    if str(numero)[5:] == '909':
        print('CONTESTAR')
    else:
        print('NO CONTESTAR')
elif hora >= 14 and hora < 17:
    if str(numero)[0:3] == '877':
        print('CONTESTAR')
    else:
        print('NO CONTESTAR')
elif hora >=17 and hora < 19:
    if str(numero)[0:3] == '877':
        print('NO CONTESTAR')
    else:
        print('CONTESTAR')
elif hora >=19 and hora < 23:
    print('NO CONTESTAR')
