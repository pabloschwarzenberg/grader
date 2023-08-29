numero=int(input('Escribe el numero de telefono: '))
hora=int(input('Escribe la hora: '))

if (0<=hora<7):
    print('CONTESTAR')
if (7<=hora<14) and ((numero%1000) != 909):
    print('NO CONTESTAR')
if (7<=hora<14) and ((numero%1000) == 909):
    print('CONTESTAR')
if (17<=hora<19) and ((numero//100000) != 877):
    print('CONTESTAR')
if (17<=hora<19) and ((numero//100000) == 877):
    print('NO CONTESTAR')
if (19<=hora<=23):
    print('NO CONTESTAR')
      