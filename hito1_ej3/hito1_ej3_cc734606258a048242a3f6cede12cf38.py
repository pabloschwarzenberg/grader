ingresos=int(input())
naci=int(input())
num=int(input())
ban=int(input())
esta=str(input())
lugar=str(input())

if ban > 10 and num > 1:
    print('APROBADO')
elif esta == 'C' and num > 3:
    if naci<1978 and naci>1966:
        print('APROBADO')
    else:
        print('RECHAZADO')
elif ingresos > 2500000 and esta == 'S' and lugar == 'U':
    print('APROBADO')
elif ingresos > 3500000 and ban > 5:
    print('APROBADO')
elif lugar=='R' and esta=='C' and num<2:
    print('APROBADO')
else:
    print('RECHAZADO')