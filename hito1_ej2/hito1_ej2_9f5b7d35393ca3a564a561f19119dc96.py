#Contestador de celular
n=eval(input('Ingresa el numero de telefono: '))
h=eval(input('ingresa la hora de llamada: '))

if 0<n<100000000 and 0<=h<=7:
    print('CONTESTAR')

if (((((n%10000000)%1000000)%100000)%10000)%1000) !=909 and 8<=h<=14:
    print('NO CONTESTAR')
else:
    if (((((n%10000000)%1000000)%100000)%10000)%1000)==909 and 8<=h<=14:
        print('CONTESTAR')

if 0<n<100000000 and 15<=h<=16:
    print('NO CONTESTAR')

if  (n-(((n%10000000)%1000000)%100000))==87700000 and 17<=h<=19:
    print('NO CONTESTAR')
else:
    if (n-(((n%10000000)%1000000)%100000))!=87700000 and 17<=h<=19:
        print('CONTESTAR')
    
if 0<n<100000000 and 20<=h<=23:
    print('NO CONTESTAR')
