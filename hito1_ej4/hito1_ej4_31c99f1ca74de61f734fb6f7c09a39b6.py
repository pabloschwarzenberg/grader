#Conversión de Decimal a Binario
n = int(input())
list = []
while (n > 0):
  remainder = n%2
  n = int(n/2)
  list.insert(0, remainder)

nBinary = ''
for x in list:
    nBinary = nBinary + str(x)
print('resultado='+nBinary)