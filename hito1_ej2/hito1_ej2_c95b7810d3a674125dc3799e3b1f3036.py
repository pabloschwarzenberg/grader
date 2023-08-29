#Contestador de celular
# entrada
x = int(input('ingrese un numero de telefono: '))
y = int(input('ingrese la hora de su llamada: '))

# procesamiento
if y>=24 or y<0:
    print('NO CONTESTAR')
elif x<=10000000 or x>=99999999:
    print('no pueden marcar numeros menos o mas de 8 digitos')
else:
    ult=x%1000
    if y>19:
        print('NO CONTESTAR')
    elif y>0 and y<7:
        print('CONTESTAR')
    elif y>17 and y<19 and ult==909:
        print('CONTESTAR')
    elif y<=14 and ult==909:
        print('CONTESTAR')
    else:
        print('NO CONTESTAR')