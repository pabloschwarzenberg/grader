#Descomponer un número
x=eval(input('ingrese numero maximo 4 digitos: '))

mil=x//1000
cien=(x//100)%10
diez=(x//10)%10
uno=(x%10)

if 1000<=x<10000:
    print(mil,'M','+', cien,'C','+',diez,'D','+',uno,'U',)
if 10<=x<100:
    print(diez,'D','+',uno,'U',)
if 1<=x<10:
    print(uno,'U',)
if 100<=x<1000:
    print(cien,'C','+',diez,'D','+',uno,'U',)

      