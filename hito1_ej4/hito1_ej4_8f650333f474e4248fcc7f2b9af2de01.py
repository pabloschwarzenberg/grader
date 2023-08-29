#Conversión de Decimal a Binario

a = int(input())

binario = ''
while a // 2 != 0:
    binario = str(a % 2) + binario
    a = a // 2
b = (str(a) + binario)

print("resultado=", int(b))