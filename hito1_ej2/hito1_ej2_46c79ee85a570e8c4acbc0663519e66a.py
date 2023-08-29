#Contestador de celular
telefono = int(input('Ingrese un numero telefonico: '))
hora = int(input('Ingrese hora de la llamada: '))
if 10000000 <= telefono <= 99999999 and 0 <= hora <= 23:
    if 0 <= hora <= 7:
        print('CONTESTAR')
    if 7 < hora < 14 and telefono%1000 == 909:
        print('CONTESTAR')
    if 17 <= hora <= 19 and telefono//100000 != 877:
        print('CONTESTAR')
    if 17 <= hora <= 19 and telefono//100000 == 877:
        print('NO CONTESTAR')
    if 19 < hora < 23:
        print('NO CONTESTAR')
    
else:
    print('Alguno de los valores son invalidos')
