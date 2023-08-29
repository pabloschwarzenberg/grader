#Contestador de celular
x=int(input('FONO:'))
z=int(input('Hora:'))
y=x%1000
f=x//100000
if (0<=z<=7) or ( 17<=z<=19 and f!=877):
    print('CONTESTAR')
if ( 17<=z<=19 and f==877):
    print('NO CONTESTAR')
if (z<14 and y!=909):
    print('NO CONTESTAR')
if  (z<14 and y==909):
    print('CONTESTAR')
if (19<z<23):
    print('NO CONTESTAR')
