#Contestador de celular
num = str(int(input('Ingrese el numero telefonico: ')))
hora = int(input('ingrese la hora de la llamada:'))

if 0<=hora<=7 or 17<=hora<=19:
    print('CONTESTAR')

if num[5] == '9' and num[6] == '0' and num[7] == '9' and 7<hora<14:
    print('CONTESTAR')

else:
    print('NO CONTESTAR')


      