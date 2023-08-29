def decimal_a_binario(numero):
    if numero == 0:
        return "0"
    else:
        bits = []
        while numero > 0:
            bits.append(str(numero % 2))
            numero //= 2
        bits.reverse()
        return "".join(bits)

# Solicitar al usuario ingresar el número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
resultado_binario = decimal_a_binario(numero_decimal)

# Imprimir el resultado en binario
print("resultado =", resultado_binario)
