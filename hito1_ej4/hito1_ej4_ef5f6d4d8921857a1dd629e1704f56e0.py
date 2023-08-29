#Conversión de Decimal a Binario
number = int(input('Ingrese un número: '))
binary = ''
while number > 0 :
  binary = str(number % 2) + binary
  number = number // 2

print('resultado=',binary)