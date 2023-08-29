#Conversión de Decimal a Binario
numero = int(input("Ingrese un número: "))
binario = []
while numero > 0:
  digito = numero % 2
  binario.append(str(digito))
  numero = numero // 2
binario.reverse()
print("resultado=" +''.join(binario))