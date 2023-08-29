#Descomponer un número
digito=int(input('ingrese un numero de 4 digitos: '))

mil=digito//1000
cent=digito%1000
cent1=cent//100
dec=digito%100
dec1=dec//10
uni=digito%10

if digito<=9:
    print(uni,str('U'))

if digito<=99:
    print(dec1,str('D +'),uni,str('U'))
if digito<=999:
    print(cent1,str('C +'),dec1,str('D +'),uni,str('U'))
if digito<=9999:
    print(mil,str('M +'),cent1,str('C +'),dec1,str('D +'),uni,str('U'))
else:
    print('el numero es mayor a 4 digitos')
   

    
     