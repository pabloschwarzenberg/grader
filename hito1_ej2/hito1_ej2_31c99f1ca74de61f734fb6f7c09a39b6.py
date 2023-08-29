#Contestador de celular
numeroTelefonico = int(input('Ingrese numero telefonico: '))
hora = int(input('Ingrese hora de la llamada: '))

resultado = ''
if 0 <= hora <= 7:
    resultado = 'CONTESTAR'
elif 14 > hora:
    if (numeroTelefonico % 1000) == 909: resultado = 'CONTESTAR'
    else: resultado = 'NO CONTESTAR'
elif 17 <= hora <= 19:
    if (numeroTelefonico // 100000) == 877: resultado = 'NO CONTESTAR'
    else: resultado = 'CONTESTAR'
else:
    resultado = 'NO CONTESTAR'

print('Resultado:', resultado)