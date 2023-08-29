def decimal_a_binario(numero):
    if numero == 0:
        return "0"
    
    binario = ""
    
    while numero > 0:
        binario = str(numero % 2) + binario
        numero = numero // 2
    
    return binario

# Pedimos al usuario que ingrese el número decimal
numero_decimal = int(input("Ingresa un número decimal: "))

# Convertimos el número decimal a binario
resultado_binario = decimal_a_binario(numero_decimal)

# Imprimimos el resultado
print("resultado =", resultado_binario)

      