#Contestador de celular
tel=int(input('ingrese número telefónico: '))
hrs=int(input('ingrese hora de la llamada: '))

if ((10000000<=tel<=99999999)and(0<=hrs<=23)):
    if 0<=hrs<=7:
        print('CONTESTAR')
    if 7 < hrs <= 14:
        tresUltimosDigitos = tel%1000
        if tresUltimosDigitos == 909:
            print('CONTESTAR')
        else:
            print('NO CONTESTAR')
    if 14 < hrs < 17:
        print('NO CONTESTAR')
    if 17 <= hrs <= 19:
        tresPrimerosDigitos = tel // 100000
        if tresPrimerosDigitos == 877:
            print('NO CONTESTAR')
        else:
            print('CONTESTAR')
    if 19 < hrs <= 23:
        print('NO CONTESTAR')
else:
    print('E R R O R')