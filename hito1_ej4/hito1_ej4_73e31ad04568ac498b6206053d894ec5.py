#Conversión de Decimal a Binario
def decimal_binario(decimal):
    if decimal == 0:
        return "0"
    
    binario = ""
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    
    return binario

numero_decimal = int(input("Ingrese un número decimal: "))

resultado_N_binario = decimal_binario(numero_decimal)

print("Resultado =", resultado_N_binario)
      