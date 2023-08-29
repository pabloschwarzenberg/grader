#Conversión de Decimal a Binario
num = int(input("Ingrese un número:"))
resultado = ''
binario = []
if num == 0:
  binario = [0]
while num > 0:
  bit = num % 2
  num = int(num/2)
  binario.insert(0,str(bit))

binario = ''.join(binario)
print("resultado=",binario)
      