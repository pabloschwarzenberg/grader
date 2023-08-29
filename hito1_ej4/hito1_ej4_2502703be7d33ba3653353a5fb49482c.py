#Conversión de Decimal a Binario

def decimal_a_binario(decimal):
    if decimal == 0:
        return "0"
    elif decimal < 0:
        return "-" + decimal_a_binario(-decimal)
    else:
        binario = ""
        while decimal > 0:
            binario = str(decimal % 2) + binario
            decimal = decimal // 2
        return binario

# Solicitar entrada al usuario
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir a binario
resultado_binario = decimal_a_binario(numero_decimal)

# Imprimir resultado
print("Resultado =", resultado_binario)
