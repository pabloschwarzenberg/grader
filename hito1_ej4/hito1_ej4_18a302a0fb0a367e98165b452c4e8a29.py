#Conversión de Decimal a BinariO
numero_decimal = int(input("ingrese un numero: "))
numero_binario = 0
multiplicador = 1
while numero_decimal != 0:       
    numero_binario = numero_binario + numero_decimal % 2 * multiplicador
    numero_decimal //= 2
    multiplicador *= 10
print("resultado = {}".format(numero_binario)) 