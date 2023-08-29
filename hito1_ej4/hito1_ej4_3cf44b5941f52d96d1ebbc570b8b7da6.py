def decimal_a_binario(decimal):
    if decimal == 0:
        return "0"  # Si el número decimal es cero, su representación binaria es "0"

    binario = ""
    
    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        decimal = decimal // 2
    
    return binario

# Ejemplo de uso:
numero_decimal = int(input("Ingrese un número decimal: "))
resultado = decimal_a_binario(numero_decimal)
print("Resultado =", resultado)