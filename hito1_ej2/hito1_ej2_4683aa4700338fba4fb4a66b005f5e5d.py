#Contestador de celular
numero = input('Ingrese numero telefonico: ')
hora = int(input('Ingrese hora de la llamada: '))

resultado = ''

if hora >= 0 and hora <= 7:
    resultado = 'CONTESTAR'

elif hora < 14:
    if numero[-3:] == '909':
        resultado = 'CONTESTAR'
    
    else:
        resultado = 'NO CONTESTAR'
    
elif hora >= 17 and hora <= 19:
    if numero[:3] == '877':
        resultado = 'NO CONTESTAR'
    else:
        resultado = 'CONTESTAR'

elif hora > 19:
    resultado = 'NO CONTESTAR'

print('Resultado: '+resultado)
