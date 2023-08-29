#Conversión de Decimal a Binario
def decimal_a_binario(numero):
    binario = ""
    
    if numero == 0:
        binario = "0"
    
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero = numero // 2
    
    return binario

numero_decimal = int(input("Ingrese un número decimal: "))
resultado = decimal_a_binario(numero_decimal)
print("resultado =", resultado)      