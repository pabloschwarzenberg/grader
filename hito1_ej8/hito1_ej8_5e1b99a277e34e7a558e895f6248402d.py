#Descomponer un número
numeroi= int(input('ingresa un numero de hasta 4 digitos: '))

d1 = numeroi%10
numero = numeroi//10

d2 = numero%10
numero = numero//10

d3 = numero%10
numero = numero//10

d4 = numero%10

if 1000<=numeroi<=9999:
    respaldosinespacio= str(d4)+'M +  ' + str(d3)+ 'C + ' + str(d2)+ 'D + ' + str(d1)+ 'U'
    print (respaldosinespacio)
else:
    if 100<=numeroi<=999:
        respaldosinespacio2= str(d3)+ 'C + ' + str(d2)+ 'D + ' + str(d1)+ 'U'
        print(respaldosinespacio2)
    else:
        if 10<=numeroi<=99:
            respaldosinespacios3= str(d2)+ 'D + ' + str(d1)+ 'U'
            print(respaldosinespacios3)
        else:
            if 0<=numeroi<=9:
                respaldosinespacios4= str(d1)+ 'U'
                print(respaldosinespacios4)