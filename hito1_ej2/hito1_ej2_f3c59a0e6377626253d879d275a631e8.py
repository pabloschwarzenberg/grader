#Contestador de celular
y=int(input('Ingrese un numero telefonico:'))
x=int(input('Ingrese la hora de llamada:'))

if 10000000<=y<=99999999 and 0<=x<=23 :
    if 0<=x<=7:
        print('Resultado: CONTESTAR')
    if 8<=x<=14:
        f = y % 1000
        if f == 909:
            print('Resultado: CONTESTAR')
        else:
            print('Resultado: NO CONTESTAR')
    if 15<=x<=16:
        print('Resultado: NO CONTESTAR')
        
    if 17 <= x <= 19:          
        tresPrimerosDigitos = y //100000   
        if tresPrimerosDigitos == 877:
            print('Resultado: NO CONTESTAR')
        else:
            print('Resultado: CONTESTAR')


    if 20<=x<=23:
        print('Resultado: NO CONTESTAR')
        
      
else:
    print('ERROR: TELEFONO U HORA DE LLAMADA ES INVALIDO')     