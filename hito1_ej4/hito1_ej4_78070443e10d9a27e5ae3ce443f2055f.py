def decimal_a_binario(numero):
    if numero == 0:
        return '0'
    bits = []
    while numero > 0:
        bits.append(str(numero % 2))
        numero = numero // 2
    bits.reverse()
    return ''.join(bits)

numero_d = int(input("Ingresa un número: "))
resultado_bin = decimal_a_binario(numero_d)
print("Resultado =", resultado_bin)