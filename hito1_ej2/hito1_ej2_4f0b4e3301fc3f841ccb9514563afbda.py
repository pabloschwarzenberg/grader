#Contestador de celular
numero=int(input('ingrese numero telefonico: '))
hora=int(input('ingrese la hora: '))
if  10000000 <= numero <= 99999999 and hora <=23:
    if  0<=hora<=7:
        print('Resultado: CONTESTAR')

    if 8 <= hora <= 14  :
        ultimosdigitos= numero%1000
        if ultimosdigitos ==909 :
            print('Resultado: CONTESTAR')
        else:
            print('Resultado: NO CONTESTAR')
    if 15<=hora<=16:
        print('Resultado: NO CONTESTAR')
        
    if 17 <= hora <= 19 :
        primerosdigitos= numero//100000
        if primerosdigitos==877:
            print('Resultado: NO CONTESTAR')
        else:
            print('Resultado: CONTESTAR')
            
    if 20<= hora <=23:
        print('Resultado: NO CONTESTAR')

        
else:
    print('Uno o mas datos invalidos')