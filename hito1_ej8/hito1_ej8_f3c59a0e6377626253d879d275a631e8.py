#Descomponer un número
numero=int(input('Ingrese un numero de 4 cifras:'))

z=numero//1000
numero=numero%1000
t=numero//100
numero=numero%100
f=numero//10
numero=numero%10

if 0<z and 0<t and 0<f and 0<numero:
    print(z,'M +',t,'C +',f,'D +',numero,'U')
if 0==z and 0<t and 0<f and 0<numero:
    print(t,'C +',f,'D +',numero,'U')
if 0==z and 0==t and 0<f and 0<numero:
    print(f,'D +',numero,'U')
if 0==z and 0==t and 0==f and 0==numero:
    print('Error')
           