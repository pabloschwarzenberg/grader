#Contestador de celular
n = int(input('Ingrese numero de 8 cifras: '))
h = int(input('Ingrese la hora de la llamada: '))

if 10000000 <= n <= 99999999 and 0 <= h <= 23:

    if 0<=h<=7:
        print('CONTESTAR')
    elif 8<=h<14 and n%1000==909:
        print('CONTESTAR')
    elif 7<h<14 and n%1000!=909:
        print('NO CONTESTAR')
    elif 14<=h<17:
        print('NO CONTESTAR')
    elif 17<=h<=19 and n%1000!=877:
        print('NO CONTESTAR')
    elif 17<=h<=19 and n%1000==877:
        print('CONTESTAR')
    elif 20<=h<=23:
        print('NO CONTESTAR')

else:
    print('ERROR: telefono u hora de llamada invalido')

      