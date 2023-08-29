#Contestador de celular
numero = int(input('Ingrese numero telefonico: '))
hora_llamada = int(input('Ingrese hora de la llamada: '))

if (hora_llamada > 23) or (hora_llamada < 0):
    print('Hora no valida')

if hora_llamada <= 7:
    print('CONTESTAR')
elif hora_llamada < 14:
    ultimos_tres_digitos = str(numero)[-3:]
    if ultimos_tres_digitos == '909':
        print('CONTESTAR')
    else:
        print('NO CONTESTAR')
elif hora_llamada >= 17 and hora_llamada <= 19:
    primeros_tres_digitos = str(numero)[:3]
    if primeros_tres_digitos == '877':
        print('NO CONTESTAR')
    else:
        print('CONTESTAR')

elif hora_llamada > 19:
    print('NO CONTESTAR')