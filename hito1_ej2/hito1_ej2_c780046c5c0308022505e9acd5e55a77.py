#Contestador de celular
numero = int(input(''))
hora = int(input(''))

if hora<=14:
    if numero%1000==909 or 0<=hora<=7:
        print('CONTESTAR')
    else:
        print('NO CONTESTAR')
elif 17<=hora<=19:
    if numero//100000==877:
        print('NO CONTESTAR')
    else:
        print('CONTESTAR')
else:
    print('NO CONTESTAR')