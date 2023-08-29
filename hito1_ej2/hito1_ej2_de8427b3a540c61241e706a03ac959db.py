#Contestador de celular
n = int(input('ingrese numero de 8 cifras:'))
h = int(input('ingrese la hora de la llamada:'))

if 10000000 <= n <= 99999999 and 0 <= h <=23:

    if 0<=h<=7:
        print('contestar')
    elif 8<=h<14 and n%1000==909:
        print('contestar')
    elif 7<h<14 and n%1000!=909:
        print('no contestar')
    elif 14<=h<17:
        print('no contestar')
    elif 17<=h<=19 and n%1000!=877:
        print('no contestar')
    elif 17<=h<=19 and n%1000==877:
        print('contestar')
    elif 20<=h<=23:
        print('no contestar')

else:
    print('ERROR: telefono u hora de llamada invalida')