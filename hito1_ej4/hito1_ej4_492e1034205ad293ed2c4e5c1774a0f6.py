def decimal_a_binario(decimal):
    binario = ""
    
    if decimal == 0:
        binario = "0"
    
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    
    return binario

# Solicitar el número decimal al usuario
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir a binario y mostrar el resultado
resultado = decimal_a_binario(numero_decimal)
print("Resultado =", resultado)