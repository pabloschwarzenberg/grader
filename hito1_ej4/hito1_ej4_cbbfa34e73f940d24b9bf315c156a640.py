#Conversión de Decimal a Binario
def decimal_a_binario(decimal):
    binario = bin(decimal)[2:]
    return binario
numero_decimal = int(input("Ingrese un número decimal: "))
numero_binario = decimal_a_binario(numero_decimal)
print("resultado =", numero_binario)