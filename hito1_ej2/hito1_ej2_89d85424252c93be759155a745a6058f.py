#Contestador de celular
num_tel = input('Ingrese numero telefonico: ')[0:8]
hora = int(input('Ingrese hora de la llamada: '))

if hora < 14 and num_tel[-1] == '9' and num_tel[-2] == '0' and num_tel[-3] == '9':
    print('CONTESTAR_1')
    pass
elif hora >= 17 and hora <= 19 and num_tel[0] == '8' and num_tel[1] == '7' and num_tel[2] == '7':
    print('NO CONTESTAR')
    pass
elif (hora > 0 and hora < 7) or (hora >= 17 and hora <= 19):
    print('CONTESTAR_3')
    pass
elif hora > 19 and hora <= 23:
    print('NO CONTESTAR')
    pass