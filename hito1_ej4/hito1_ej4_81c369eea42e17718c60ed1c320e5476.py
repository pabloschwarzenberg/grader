#Conversión de Decimal a Binario
n_decimal = eval(input("Ingrese un numero: "))
binario = 0
i = 1

while n_decimal != 0:
    binario = binario + n_decimal % 2 * i
    n_decimal //= 2
    i *= 10

print("resultado =", binario)
