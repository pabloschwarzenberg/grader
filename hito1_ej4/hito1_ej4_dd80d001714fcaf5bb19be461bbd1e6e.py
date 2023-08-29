#Conversión de Decimal a Binario
n = int(input('ingresa numero: '))
b = ''

while n != 0:
    b = str(n%2)+b
    n = n//2
    
print('resultado=',b)