def decimal_a_binario(numero):
    if numero == 0:
        return "0"
    else:
        binario = ""
        while numero > 0:
            residuo = numero % 2
            binario = str(residuo) + binario
            numero = numero // 2
        return binario

# Solicitar número decimal al usuario
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir a binario
resultado = decimal_a_binario(numero_decimal)

# Imprimir resultado
print("resultado=" + resultado)