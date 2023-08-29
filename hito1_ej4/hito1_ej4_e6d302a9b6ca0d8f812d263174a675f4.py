#Conversión de Decimal a Binario
n = int(input('Ingresa un numero: '))
bi=''
while n // 2 != 0:
  bi = str(n % 2) + bi
  n = n // 2
  binario= str(n) + bi
print("resultado=",binario)