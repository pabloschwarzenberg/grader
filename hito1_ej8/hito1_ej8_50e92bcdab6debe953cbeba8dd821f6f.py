#Descomponer un número
x=int(input('Ingrese un número de 4 digitos:'))
x4=x//1000
x3=x//100%10
x2=x%100//10
x1=x%10

if 0 <= x < 10  :
     print(x4,'U')
elif 10 <= x < 100:
    print(x2, 'D + ', x1, 'U')
elif 100<x<1000:
    print(x3, 'C + ', x2, 'D + ', x1, 'U')
elif 1000 <= x < 10000:
    print(x4 ,'M + ', x3, 'C + ', x2, 'D +' , x1, 'U')

