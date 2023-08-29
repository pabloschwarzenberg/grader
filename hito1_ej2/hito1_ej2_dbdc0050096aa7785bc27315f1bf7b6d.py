#Contestador de celular
numero = input('Ingrese numero telefonico: ')
hora_llamada = int(input('Ingrese hora de la llamada: '))

num_list = list(numero)

if hora_llamada >= 0 and hora_llamada <= 7:
    print('CONTESTAR')

elif hora_llamada < 14:
    if num_list[5:9] == ['9','0','9']:
        print('CONTESTAR')
    else:
        print('NO CONTESTAR')

elif hora_llamada >= 17 and hora_llamada <= 19:
    if num_list[0:3] != ['8','7','7']:
        print('CONTESTAR')
    elif num_list[0:3] == ['8','7','7']:
        print('NO CONTESTAR')

elif hora_llamada > 19 :
    print('NO CONTESTAR')