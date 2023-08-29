#Conversión de Decimal a Binario
def decimal_a_binario(numero):
    if numero == 0:
        return '0'
    bits = []
    while numero > 0:
        bits.append(str(numero % 2))
        numero = numero // 2
    bits.reverse()
    return ''.join(bits)

numero_decimal = int(input("Ingrese un número decimal: "))

resultado_binario = decimal_a_binario(numero_decimal)
print("resultado =", resultado_binario)
      