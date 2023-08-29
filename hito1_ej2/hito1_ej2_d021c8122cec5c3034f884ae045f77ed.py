#Contestador de celular
tel=int(input('ingrese numero telefonico: '))
hora=int(input('ingrese hora de la llamada: '))

if 10000000 <=tel <=99999999 and 0<=hora<=23:
    
    if hora>=0 and hora<=7:
        print('Contestar') 
    elif hora>=8 and hora<14:
        tresUlt = tel%1000
        if tresUlt==909:
            print('Contestar')
        else:           
            print('No Contestar')
    elif hora>=17 and hora<=19:
        tresPrim= tel//10000
        if tresPrim==877:
            print('Contestar')
        else:
            print('No Contestar')
    elif hora>=19:
        print('No Contestar')
else:
    print('ingrese los datos correctamente')      