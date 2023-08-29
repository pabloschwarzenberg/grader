def decimal_a_binario(numero):
    if numero == 0:
        return '0'
    
    bits = []
    
    while numero > 0:
        bit = numero % 2
        bits.append(str(bit))
        numero = numero // 2
    
    bits.reverse()
    resultado = ''.join(bits)
    return resultado

# Solicitar al usuario el número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario utilizando la función decimal_a_binario
resultado_binario = decimal_a_binario(numero_decimal)

# Imprimir el resultado binario
print("Resultado =", resultado_binario)
      