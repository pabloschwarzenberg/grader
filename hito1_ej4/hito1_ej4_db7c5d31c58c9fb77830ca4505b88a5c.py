#Conversión de Decimal a Binario
def decimal_a_binario(decimal):
    es_negativo = False
    if decimal < 0:
        es_negativo = True
        decimal = abs(decimal)
    
    if decimal == 0:
        return "0"
    
    binario = ""
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    
    if es_negativo:
        binario = "-" + binario
    
    return binario

numero_decimal = int(input("Ingrese un número decimal: "))  # Cambiado a int
resultado = decimal_a_binario(numero_decimal)
print("resultado =", resultado)