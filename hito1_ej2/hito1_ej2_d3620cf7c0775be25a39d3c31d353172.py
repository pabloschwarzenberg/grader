#CONTESTADOR AUTOMATICO
XXXXXXXX = int(input('Ingrese número telefónico: '))
Y = int(input('ingrese hora de la llamada: '))

caso1 = XXXXXXXX%1000
caso2 = XXXXXXXX//100000

if 0 <= Y <= 7:
    print('CONTESTAR')
if 7 <= Y < 14:
    if caso1 == 909:
        print('CONTESTAR')
    else:
        print('NO CONTESTAR')
if 17 <= Y <= 19:
    if caso2 == 877:
        print('NO CONTESTAR')
    else:
        print('CONTESTAR')
if 19 <= Y <= 23:
    print ('NO CONTESTAR')
 