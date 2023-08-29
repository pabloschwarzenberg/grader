#Contestador de celular
telefono = int(input('Ingrese numero telefonico: '))
hora = int(input('Ingrese hora de la llamada (formato 0, 23): '))

comienzo = telefono//100000

final = telefono%1000


if hora >= 0 and hora <=7:
    print('CONTESTAR')


elif hora <= 14 and final == 909:
    print('CONTESTAR')

elif hora >= 17 and hora <= 19 and comienzo == 877:
    print('NO CONTESTAR')

elif hora >= 17 and hora <= 19:
    print('CONTESTAR')

elif hora > 19:
    print('NO CONTESTAR')