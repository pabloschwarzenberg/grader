#Conversión de Decimal a Binario
def binary(num):
  if num > 1:
    binary(num//2)
    print(num%2, end='')
    
binary(33)      