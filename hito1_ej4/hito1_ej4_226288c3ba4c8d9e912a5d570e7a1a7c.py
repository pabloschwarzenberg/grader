#Conversión de Decimal a Binario
def decimal_a_binario(numero):
    if numero == 0:
        return "0"  # Caso especial para el número 0
    else:
        binario = ""
        while numero > 0:
            residuo = numero % 2
            binario = str(residuo) + binario
            numero = numero // 2
        return binario

# Pedimos al usuario que ingrese el número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertimos el número decimal a binario
numero_binario = decimal_a_binario(numero_decimal)

# Imprimimos el resultado
print("resultado=" + numero_binario)  