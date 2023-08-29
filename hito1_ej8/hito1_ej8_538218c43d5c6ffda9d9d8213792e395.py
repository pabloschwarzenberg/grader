x=int(input('Ingrese un numero positivo de maximo 4 digitos: '))

u= x
U=x%10
d= ((x-U)/10)
c= ((x-x%100)/100)
m= ((x-x%1000)/1000)

if x<0:
    print('Digitaste un numero negativo')
elif 9999<x:
    print('Digitaste un numero de cinco digitos o mas')
elif 0<=x<=9 :
    print('',int(u), 'U')
elif 10<=x<=99: 
    print('',int(d),'D','+',int(U),'U')
elif 100<=x<=999:
    print('', int(c),'C','+',int(d%10),'D','+',int(U),'U')
elif 1000<=x<=9999:
     print('',int(m), 'M','+', int(c%10),'C','+',int(d%10),'D','+',int(U),'U')

      