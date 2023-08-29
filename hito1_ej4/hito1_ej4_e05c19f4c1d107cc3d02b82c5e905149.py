#Conversión de Decimal a Binario
n = int(input())
b = ''

while n != 0:
  b += str(n % 2)
  n //= 2
  
print('resultado={}'.format(b[::-1]))