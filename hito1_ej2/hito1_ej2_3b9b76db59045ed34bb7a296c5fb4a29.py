#Contestador de celular

print('Ingrese la hora y el número de la llamada.')

numero=int(input('Ingrese el número telefonico: '))
hora=int(input('Ingrese la hora de la llamada: '))

if 0<=hora<=23 and 10000000<=numero<=99999999:
    if 0<=hora<=7:
        print('CONTESTAR')
    if 7<hora<=14:
        if numero%1000==909:
            print('CONTESTAR.')
        else:
            print('NO CONTESTAR.')
    if 14<hora<=17:
        print('NO CONTESTAR.')
    if 17<hora<=19:
        if numero//100000==877:
            print('NO CONTESTAR.')
        else:
            print('CONTESTAR.')
    if 19<hora<=23:
        print('NO CONTESTAR.')
else:
    print('ERROR,Ingrese una hora o un número validos.')
