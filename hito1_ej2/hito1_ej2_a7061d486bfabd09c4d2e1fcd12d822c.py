#Contestador de celular

tel = str(input('Ingrese su número de teléfono: '))
hora = int(input('Ingrese la hora de la llamda: '))

if 0 < hora <= 7:
        print('CONTESTAR')
elif 7 < hora <= 14 and (tel.endswith('909')):
        print('CONTESTAR')
else:
        print('NO CONTESTAR')
if 17 < hora < 19 and (tel.startswith('877')):
        print('CONTESTAR')
else: 
        print('NO CONTESTAR')
if hora >= 19:
        print('NO CONTESTAR')      