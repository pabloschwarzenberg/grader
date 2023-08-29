#Contestador de celular
numero=int(input('ingrese el numero'))
hora=float(input('ingrese la hora'))
if 0<=hora<=7:
    print('CONTENTAR')
if 7<hora<14:
    if numero%1000==909:
        print('CONTESTAR')
    else:
        print('NO CONTESTAR')
if 17<=hora<=19:
    if numero//100000==877:
        print('NO CONTESTAR')
    else: 
        print('CONTESTAR')
if 19<hora<23.59:
    print('NO CONTESTAR')