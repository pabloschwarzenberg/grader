#Contestador de celular
num= input("Ingrese numero telefonico: ")
hora= int(input("Ingrese hora de llamada: "))
if hora > 0  and hora <=7:
    print('CONTESTAR')

elif hora > 7 and hora < 14:
    if num[5]=='9':
        if num[6]=='0':
            if num[7]=='9':
                print('CONTESTAR')
            else:
                print('NO CONTESTAR')
        else:
            print('NO CONTESTAR')
    else:
        print('NO CONTESTAR')

elif hora >=17 and hora <= 19:
    if num[0]=='8':
        if num[1]=='7':
            if num[2]=='7':
                print('NO CONTESTAR')
            else:
                print('CONTESTAR')
        else:
            print('CONTESTAR')
    else:
        print('CONTESTAR')

elif hora >= 19:
    print('NO CONTESTAR')