#Conversión de Decimal a Binario
num = int(input('Ingresa un número: '))
list = list(str(bin(num)))
list.remove('0')
list.remove('b')
print('resultado='+''.join(list))