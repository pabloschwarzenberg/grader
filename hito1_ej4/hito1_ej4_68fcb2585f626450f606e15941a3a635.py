x = int(input("Ingrese un número decimal: "))
binario = []
while x > 0:
    digito = x % 2
    binario.append(str(digito))
    x = x// 2
binario.reverse()

print("resultado=" +''.join(binario))