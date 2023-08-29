#Contestador de celular

t=int(input('ingresa un numero telefonico:'))
h=int(input('ingresa la hora de la llamada:'))
if 10000000<= t<=99999999 and 0<=h<=23:
    if 0<=h<=7:
        print('resultado:CONTESTAR')
    if 7<h<=14 and t%1000!=909:
        print('resultado: NO CONTESTAR')
    if t%1000==909 and 7<h<=14:
        print('resultado:CONTESTAR')
    else:
        print('resultado: NO CONTESTAR')    
    if 15<=h<17:
       print('resultado: NO CONTESTAR')
    if 17<=h<=19:
        print('resultado:CONTESTAR')
        if t//100000==877:
            print('resultado: NO CONTESTAR')
        else:
            print('resultado:CONTESTAR')
    if 19<h<=23:
        print('resultado: NO CONTESTAR')
else:
    print('al menos uno de los datos no es correcto')
         