#Conversión de Decimal a Binario
def decimal_a_binario(numero):
    binario = ""

    if numero == 0:
        binario = "0"
    else:
        while numero > 0:
            binario = str(numero % 2) + binario
            numero //= 2

    return binario

numero_decimal = int(input("Ingrese un número decimal: "))

resultado_binario = decimal_a_binario(numero_decimal)

print("resultado =", resultado_binario)
      