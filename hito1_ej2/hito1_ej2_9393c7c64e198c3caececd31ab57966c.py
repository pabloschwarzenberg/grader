#Contestador de celular
num = input('\nIngrese numero telefónico:')
hora = int(input('\nIngrese hora de la llamada:'))
if len(num) == 8:
    if int(num[5:8]) == 909 and hora < 14:
        print('Resultado: CONTESTAR')
    elif 0 < hora < 7:
        print('Resultado: CONTESTAR')
    elif int(num[0:3]) != 877 and 17 < hora < 19:
        print('Resultado: CONTESTAR')
    elif int(num[0:3]) == 877 and 17 < hora < 19:
        print('Resultado: NO CONTESTAR')
    else:
        print('Resultado: NO CONTESTAR')
else:
    print('Resultado: NO CONTESTAR')      