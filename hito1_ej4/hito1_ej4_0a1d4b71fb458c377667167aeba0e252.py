import math

decimal = int(input("Ingresa un número decimal: "))
binario = ""
potencia = int(math.log(decimal, 2))
for i in range(potencia, -1, -1):
    if decimal >= 2 ** i:
        binario += "1"
        decimal -= 2 ** i
    else:
        binario += "0"
print("resultado=" + binario)
