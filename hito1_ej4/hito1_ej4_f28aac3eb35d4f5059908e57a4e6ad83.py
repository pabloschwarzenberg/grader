def decimal_a_binario(decimal):
    if decimal == 0:
        return "0"

    binario = ""
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal //= 2

    return binario

# Solicitar al usuario el número decimal
decimal = int(input("Ingrese un número decimal: "))

# Convertir a binario
resultado = decimal_a_binario(decimal)

# Imprimir el resultado
print("resultado=" + resultado)