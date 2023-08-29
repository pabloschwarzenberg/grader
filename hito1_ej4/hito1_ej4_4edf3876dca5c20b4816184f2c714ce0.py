#Conversión de Decimal a Binario   
a = int(input('conversor decimal a binario: '))

I = list(bin(a))
I.pop(0)
I.remove('b')

a = ''.join(I)
print('resultado=',a)