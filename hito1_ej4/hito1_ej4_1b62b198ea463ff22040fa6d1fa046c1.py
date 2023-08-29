#Conversión de Decimal a n=int(input("Ingrese un numero decimal: "))
numero = int(input("Ingrese un número: "))
binario = []
while numero > 0:
    digito = numero % 2
    binario.append(str(digito))
    numero = numero // 2
binario.reverse()

print("resultado=" +''.join(binario))
