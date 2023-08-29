#Conversión de Decimal a Binario
number = int(input("Ingresa un número decimal: "))
binario = ""

if number == 0:
    binario = "0"
else:
    while number > 0:
        residuo = number % 2
        binario = str(residuo) + binario
        number = number // 2

print("resultado=",binario)