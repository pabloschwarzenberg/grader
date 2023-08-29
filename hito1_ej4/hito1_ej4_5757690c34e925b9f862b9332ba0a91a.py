def decimal_a_binario(numero):
    resultado = bin(numero)[2:]
    return resultado

numero_decimal = int(input("Ingrese un número decimal: "))
resultado_binario = decimal_a_binario(numero_decimal)

print("resultado =", resultado_binario)
      