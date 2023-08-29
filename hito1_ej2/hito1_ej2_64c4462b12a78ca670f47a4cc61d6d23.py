#Contestador de celular

numero = input('Número: ')
hora = input('Hora: ')
hora = int(hora)
numero = int(numero)

if hora > 0 and hora < 7:
    print('CONTESTAR')
elif hora < 14:
    if str(numero)[5:] == str(909):
        print('CONTESTAR')
    else:
        print('NO CONTESTAR')
elif hora > 14 and hora < 17:
    print('NO CONTESTAR')
elif hora > 17 and hora <19:
    if str(numero)[:3] == str(877):
        print('NO CONTESTAR')
    else:
        print('CONTESTAR')
else:
    print('NO CONTESTAR')
