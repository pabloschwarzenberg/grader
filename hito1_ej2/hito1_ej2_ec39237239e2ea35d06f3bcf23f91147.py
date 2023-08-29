n= input('Ingrese numero telefonico:')
h= int(input('Ingrese hora de la llamada:'))
if h >= 0 and h < 7:
        print('Contestar')
elif h < 14:
        print('Contestar')
elif h <= 13 and str(numero)[-3:-4] =='909':       
        print('Contestar')
elif h >= 17 and h < 19 and not str(n).startswith('877'):
        print('Contestar')
else:
        print('no Contestar')

