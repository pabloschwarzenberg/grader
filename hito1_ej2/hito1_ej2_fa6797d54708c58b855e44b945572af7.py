#Contestador de celular
numero = int(input('Ingresa tu numero telefonico: '))
hora = int(input('Ingresa la hora de la llamada: '))

if 10000000 <= numero <= 99999999 and 0 <= hora <= 23:
    if hora <= 7 and hora >= 0:
        print('CONTESTAR')
        
    if hora <= 14 and hora > 7:
        if numero%1000 == 909:
            print('CONTESTAR')
        else:
            print('NO CONTESTAR')

    if hora >=17 and hora <19:
        if numero//100000 == 877:
            print('NO CONTESTAR')
        else:
            print('CONTESTAR')

    if hora >= 19 and hora <= 23:
        print('NO CONTESTAR')
else:
    print('Alguno de los datos es incorrecto')