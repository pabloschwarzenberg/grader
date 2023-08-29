#Conversión de Decimal a Binario
num = int(input("Ingrese un número: "))
binario = []
while num > 0:
    digito = num % 2
    binario.append(str(digito))
    num = num // 2
binario.reverse()

print("resultado=" +''.join(binario))      